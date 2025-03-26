import pandas as pd
import joblib
import json

def assign_risk_score():

    # Load datasets
    def load_datasets():
        transactions_df = pd.read_csv("data/processed_output_with_new_category.csv")
        sdn_df = pd.read_csv("data/alt.csv")
        world_bank_df = pd.read_excel("data/Sanctioned individuals and firms.xlsx")
        non_sdn_df = pd.read_csv("data/non-sdn.csv")
        return transactions_df, sdn_df, world_bank_df, non_sdn_df

    # Load trained model
    model = joblib.load("models/risk_score_model.pkl")

    def predict_risk(transaction):
        """Use trained model to predict risk score."""
        features = ["Sender Predicted Category", "Receiver Predicted Category", "Sender Country", "Receiver Country"]
        
        df = pd.DataFrame([transaction])
        df = pd.get_dummies(df)

        # Align features with model input
        missing_cols = set(model.feature_names_in_) - set(df.columns)
        for col in missing_cols:
            df[col] = 0  # Add missing columns as 0
        
        df = df[model.feature_names_in_]  # Reorder columns

        # Predict risk score
        risk_score = model.predict(df)[0]
        risk_score = round(max(0.0, min(1.0, risk_score)), 2)

        return risk_score

    def generate_risk_reasons(sender_name, receiver_name, sender_category, receiver_category, sender_country, receiver_country, sdn_df, world_bank_df, non_sdn_df):
        """Generate reasons based on entity lists, country risk, and category risk."""
        reasons = []

        #  Check OFAC SDN List (Improved Matching)
        if sdn_df["Entity Name"].astype(str).str.lower().str.contains(str(sender_name).lower(), na=False).any():
            reasons.append(f"Sender '{sender_name}' found in OFAC SDN List (Very High Risk)")

        if sdn_df["Entity Name"].astype(str).str.lower().str.contains(str(receiver_name).lower(), na=False).any():
            reasons.append(f"Receiver '{receiver_name}' found in OFAC SDN List (Very High Risk)")

        #  Check OFAC Non-SDN List
        if non_sdn_df["Entity Name"].astype(str).str.lower().str.contains(str(sender_name).lower(), na=False).any():
            reasons.append(f"Sender '{sender_name}' found in OFAC Non-SDN List (Moderate Risk)")

        if non_sdn_df["Entity Name"].astype(str).str.lower().str.contains(str(receiver_name).lower(), na=False).any():
            reasons.append(f"Receiver '{receiver_name}' found in OFAC Non-SDN List (Moderate Risk)")

        #  Check World Bank Debarred List
        if world_bank_df["Firm Name"].astype(str).str.lower().str.contains(str(sender_name).lower(), na=False).any():
            reasons.append(f"Sender '{sender_name}' found in World Bank Debarred List (High Risk)")

        if world_bank_df["Firm Name"].astype(str).str.lower().str.contains(str(receiver_name).lower(), na=False).any():
            reasons.append(f"Receiver '{receiver_name}' found in World Bank Debarred List (High Risk)")

        #  Check FATF Country Risk
        fatf_black_list = ["Democratic People's Republic of Korea", "Iran", "Myanmar"]
        fatf_grey_list = ["Algeria", "Angola", "Panama", "Nigeria", "South Africa", "Vietnam", "Yemen"]

        if sender_country in fatf_black_list:
            reasons.append(f"Sender Country '{sender_country}' is in FATF Black List (Very High Risk)")
        elif sender_country in fatf_grey_list:
            reasons.append(f"Sender Country '{sender_country}' is in FATF Grey List (Moderate Risk)")

        if receiver_country in fatf_black_list:
            reasons.append(f"Receiver Country '{receiver_country}' is in FATF Black List (Very High Risk)")
        elif receiver_country in fatf_grey_list:
            reasons.append(f"Receiver Country '{receiver_country}' is in FATF Grey List (Moderate Risk)")

        #  Check Entity Category Risk
        entity_risk = {
            "Shell Company": "Shell Company - High Risk",
            "NGO": "NGO - Moderate Risk",
            "Government Agency": "Government Agency - Low Risk",
            "PEP": "Politically Exposed Person (PEP) - Very High Risk"
        }

        if sender_category in entity_risk:
            reasons.append(f"Sender is a {entity_risk[sender_category]}")
        
        if receiver_category in entity_risk:
            reasons.append(f"Receiver is a {entity_risk[receiver_category]}")

        return reasons



    def process_transactions():
        """Process transactions, predict risk scores, and generate reasons."""
        transactions_df, sdn_df, world_bank_df, non_sdn_df = load_datasets()
        results = []
        
        for _, row in transactions_df.iterrows():
            transaction = {
                "Sender Predicted Category": row["Sender Predicted Category"],
                "Receiver Predicted Category": row["Receiver Predicted Category"],
                "Sender Country": row["Sender Country"],
                "Receiver Country": row["Receiver Country"]
            }
            
            risk_score = predict_risk(transaction)
            reasons = generate_risk_reasons(
                row["Sender Name"], row["Receiver Name"],
                row["Sender Predicted Category"], row["Receiver Predicted Category"],
                row["Sender Country"], row["Receiver Country"],
                sdn_df, world_bank_df, non_sdn_df
            )
            
            results.append({
                "Transaction ID": row["Transaction ID"],
                "Extracted Entity": [row["Sender Name"], row["Receiver Name"]],
                "Entity Type": [row["Sender Predicted Category"], row["Receiver Predicted Category"]],
                "Risk Score": risk_score,
                "Supporting Evidence": reasons,
                "Confidence Score": 0.95
            
            })
        
        return results

    # Run risk analysis and save to JSON
    risk_analysis_results = process_transactions()
    output_path = "data/risk_analysis_results.json"
    with open(output_path, "w") as json_file:
        json.dump(risk_analysis_results, json_file, indent=4)

    print(f"Risk analysis results saved to {output_path}")
