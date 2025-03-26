import pandas as pd

def get_country_risk(country):
    """Assign risk score based on receiver country."""
    fatf_black_list = ["Democratic People's Republic of Korea", "Iran", "Myanmar"]
    fatf_grey_list = ["Algeria", "Angola", "Bulgaria", "Burkina Faso", "Cameroon", "Côte d'Ivoire", "Croatia", 
                      "Democratic Republic of Congo", "Haiti", "Kenya", "Lao People's Democratic Republic", 
                      "Lebanon", "Mali", "Monaco", "Mozambique", "Namibia", "Nepal", "Nigeria", "South Africa", 
                      "South Sudan", "Syria", "Tanzania", "Venezuela", "Vietnam", "Yemen", "Panama"]

    if country in fatf_black_list:
        return 0.9
    elif country in fatf_grey_list:
        return 0.75
    return 0.05  # Default low risk

def calculate_risk(row, sdn_df, world_bank_df, non_sdn_df):
    """Calculate risk score based on defined rules."""
    risk_score = 0.0
    evidence = []

    # Check sanctions and debarred lists
    if row["Sender Name"] in sdn_df["Entity Name"].values or row["Receiver Name"] in sdn_df["Entity Name"].values:
        risk_score += 1.0
        evidence.append("OFAC SDN List")

    if row["Sender Name"] in non_sdn_df["Entity Name"].values or row["Receiver Name"] in non_sdn_df["Entity Name"].values:
        risk_score += 0.7
        evidence.append("OFAC NON-SDN List")

    if row["Sender Name"] in world_bank_df["Firm Name"].values or row["Receiver Name"] in world_bank_df["Firm Name"].values:
        risk_score += 0.5
        evidence.append("World Bank Debarred List")

    # Entity category-based risk
    category_risk = {"Shell Company": 0.85, "PEP": 0.8}
    risk_score += category_risk.get(row["Sender Predicted Category"], 0.0)
    risk_score += category_risk.get(row["Receiver Predicted Category"], 0.0)

    # Country risk
    risk_score += get_country_risk(row["Sender Country"])
    risk_score += get_country_risk(row["Receiver Country"])

    # Ensure risk score is within [0,1] range
    risk_score = max(0.0, min(1.0, risk_score))

    return risk_score

def generate_training_data():
    """Create dataset with calculated risk scores."""
    # Load datasets
    transactions_df = pd.read_csv("data/input_data/rsk_score_training_data.csv")
    sdn_df = pd.read_csv("data/dataset/alt.csv")
    world_bank_df = pd.read_excel("data/dataset/Sanctioned individuals and firms.xlsx")
    non_sdn_df = pd.read_csv("data/dataset/non-sdn.csv")

    # Calculate risk scores
    transactions_df["Risk Score"] = transactions_df.apply(lambda row: calculate_risk(row, sdn_df, world_bank_df, non_sdn_df), axis=1)

    # Save new dataset
    transactions_df.to_csv("data/training_data/training_data.csv", index=False)
    print("Training data with risk scores saved!")

generate_training_data()
