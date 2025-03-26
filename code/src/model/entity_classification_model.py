import os
import shutil
import pandas as pd
import torch
import numpy as np
from sklearn.model_selection import train_test_split
from transformers import (AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer)
from datasets import Dataset
import evaluate  #  Fixed: Replaced deprecated `load_metric`

#  Step 1: Delete Previous Trained Model Directory (if exists)
# if os.path.exists("./results"):
#     shutil.rmtree("./results")

#  Step 2: Load Transaction Dataset
# file_path = "processed_output.csv"
# df = pd.read_csv(file_path)

#  Step 3: Define Category Mapping
category_mapping = {
    "Shell Company": 0,
    "Government Organization": 1,
    "NGO": 2,
    "Corporation": 3,
    "PEP": 4
}


#  Step 4: Load Labeled Training Data (500 Examples per Category)
df_train = pd.read_csv("labeled_training_data.csv")
df_train["Category"] = df_train["Category"].map(category_mapping)

#  Step 5: Train-Test Split (Ensure Equal Representation)
train_texts, val_texts, train_labels, val_labels = train_test_split(
    df_train['Entity Name'].tolist(), df_train['Category'].tolist(), test_size=0.2, stratify=df_train["Category"], random_state=42
)

#  Step 6: Tokenization
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def tokenize_function(texts):
    return tokenizer(texts, truncation=True, padding=True, max_length=128, return_tensors="pt")

train_encodings = tokenize_function(train_texts)
val_encodings = tokenize_function(val_texts)

#  Step 7: Convert to Dataset
train_dataset = Dataset.from_dict({
    "input_ids": train_encodings["input_ids"],
    "attention_mask": train_encodings["attention_mask"],
    "labels": torch.tensor(train_labels)
})

val_dataset = Dataset.from_dict({
    "input_ids": val_encodings["input_ids"],
    "attention_mask": val_encodings["attention_mask"],
    "labels": torch.tensor(val_labels)
})

#  Step 8: Initialize Model
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=5)

#  Step 9: Define Training Arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=5,
    weight_decay=0.01,
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10
)

#  Step 10: Define Metrics
accuracy_metric = evaluate.load("accuracy")  
f1_metric = evaluate.load("f1")  

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    accuracy = accuracy_metric.compute(predictions=predictions, references=labels)
    f1_score = f1_metric.compute(predictions=predictions, references=labels, average="weighted")
    return {"accuracy": accuracy["accuracy"], "f1_score": f1_score["f1"]}

#  Step 11: Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics
)

#  Step 12: Train the Model
trainer.train()

#  Step 13: Save Trained Model & Tokenizer
model.save_pretrained("./results")
tokenizer.save_pretrained("./results")
print(" Model training completed and saved in ./results")
