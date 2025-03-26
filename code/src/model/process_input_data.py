import pandas as pd
import json
import os
import re
from transformers import pipeline

# Load the Named Entity Recognition (NER) pipeline using a BERT model
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

def process_csv(file_path):
    csv_file = "structured_data.csv"
    df = pd.read_csv(csv_file)

# Step 2: Rename and reorder columns to match 'output_format.xlsx'
    df_transformed = df.rename(columns={
        "Payer Name": "Sender Name",
        "Receiver Name": "Receiver Name",
        "Transaction ID": "Transaction ID",
        "Amount": "Amount",
        "Receiver Country": "Receiver Country",
        "Payer Country": "Sender Country",
        "Notes": "Transaction Details",
        "Date": "Date",
        "Payer Bank": "Sender Bank",
        "Receiver Bank": "Receiver Bank",
        "Status":"Status"
    })[["Transaction ID", "Date", "Sender Name", "Sender Country", "Sender Bank", "Receiver Name", "Receiver Country", "Receiver Bank", "Amount", "Transaction Details", "Status"]]

    return df_transformed

def process_json(file_path):
    with open(file_path, "r") as file:
        transactions_data = json.load(file)

    transactions_list = []
    for txn in transactions_data:
        transactions_list.append({
            "Transaction ID": txn["Transaction ID"],
            "Date": txn["Date"],
            "Sender Name": txn["Sender"]["Name"],
            "Sender Country": txn["Sender"]["Country"],
            "Sender Bank": txn["Sender"]["Bank"],
            "Receiver Name": txn["Receiver"]["Name"],
            "Receiver Country": txn["Receiver"]["Country"],
            "Receiver Bank": txn["Receiver"]["Bank"],
            "Amount": txn["Amount"],
            "Transaction Details": txn["Transaction Type"],
            "Status": txn["Status"]
        })

    df = pd.DataFrame(transactions_list)
    return df

def process_text(file_path):
    with open(file_path, "r") as file:
        unstructured_text = file.read()

    # Extract named entities from text
    ner_results = ner_pipeline(unstructured_text)

    # Combine subword tokens properly
    entities = []
    current_entity = ""
    last_position = -1

    for entity in ner_results:
        if entity['start'] - last_position > 1:  # New entity detected
            if current_entity:
                entities.append(current_entity.strip())  # Save previous entity
            current_entity = entity['word']
        else:  # Continuing the same entity
            current_entity += " " + entity['word']

        last_position = entity['end']

    # Save last detected entity
    if current_entity:
        entities.append(current_entity.strip())

    # Extract ownership information using regex
    ownership_data = []
    ownership_patterns = re.findall(r"(\bEntity\s[A-Z]\b).*?(\d+)\s*percent", unstructured_text)

    for entity, percentage in ownership_patterns:
        ownership_data.append({
            "Owner": "Blocked Person X",
            "Entity": entity.strip(),
            "Ownership Percentage": percentage + "%"
        })

    df = pd.DataFrame(ownership_data)
    return df

def process_file(input_file, output_file):
    file_extension = os.path.splitext(input_file)[1]

    if file_extension == ".csv":
        print("Processing structured CSV file...")
        df = process_csv(input_file)
    elif file_extension == ".json":
        print("Processing JSON file...")
        df = process_json(input_file)
    elif file_extension == ".txt":
        print("Processing Unstructured Text file...")
        df = process_text(input_file)
    else:
        print("Unsupported file type. Please provide a CSV, JSON, or TXT file.")
        return

    # Save output as CSV
    df.to_csv(output_file, index=False)
    print(f" Processing completed. Structured data saved as output_file")
        
    #process_file(input_file, output_file)
