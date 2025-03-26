import os
import shutil
import pandas as pd
import torch
import numpy as np
from sklearn.model_selection import train_test_split
from transformers import (AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer)
from datasets import Dataset
import evaluate  #  Fix: Replaced deprecated `load_metric`

def predict_entity(file_path):
    #  Step 2: Load Dataset
    df = pd.read_csv(file_path)

    # ------------------------------
    # 🔹 PREDICTION (Using Trained Model)
    # ------------------------------

    #  Step 14: Load the Trained Model
    model = AutoModelForSequenceClassification.from_pretrained("./results")
    tokenizer = AutoTokenizer.from_pretrained("./results")
    #  Step 3: Define Category Mapping
    category_mapping = {
        "Shell Company": 0,
        "Government Organization": 1,
        "NGO": 2,
        "Corporation": 3,
        "PEP": 4
    }
    inverse_category_mapping = {v: k for k, v in category_mapping.items()}

    #  Step 15: Prepare for Prediction (Initialize New Columns if they don't exist)
    if "Sender Predicted Category" not in df.columns:
        df["Sender Predicted Category"] = "Unknown"
    if "Receiver Predicted Category" not in df.columns:
        df["Receiver Predicted Category"] = "Unknown"

    #  Function to Predict Categories
    def predict_category(entity_name):
        if pd.isna(entity_name):
            return "Unknown"
        
        # Tokenize entity name
        tokenized_data = tokenizer(entity_name, truncation=True, padding=True, max_length=128, return_tensors="pt")

        # Perform inference
        model.eval()
        with torch.no_grad():
            outputs = model(**tokenized_data)
            prediction = torch.argmax(outputs.logits, dim=1).item()
        
        return inverse_category_mapping[prediction]

    #  Apply Predictions to Sender & Receiver
    df["Sender Predicted Category"] = df["Sender Name"].apply(predict_category)
    df["Receiver Predicted Category"] = df["Receiver Name"].apply(predict_category)

    #  Step 16: Append Updated Data to Processed File
    df.to_csv("./src/data/output_data/processed_output_with_predictions.csv", index=False)

    print(" Entity classification completed and appended to processed_output_with_predictions.csv")
