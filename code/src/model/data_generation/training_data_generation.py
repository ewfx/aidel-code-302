import pandas as pd
import random

#  Define categories
categories = ["Shell Company", "Government Organization", "NGO", "Corporation", "PEP"]

#  Example name structures for each category
category_examples = {
    "Shell Company": [
        "Panama Holdings Ltd", "Caribbean Finance Inc.", "Bahamas Investments Group", "Cayman Trust Fund",
        "British Virgin Islands Partners", "Swiss Offshore Capital", "Mauritius Asset Management",
        "Hong Kong Ventures Ltd", "Singapore Wealth Management", "Delaware Consulting LLC"
    ],
    "Government Organization": [
        "United Nations", "World Bank", "IMF", "European Central Bank", "Reserve Bank of India",
        "Federal Reserve", "Bank of England", "US Treasury Department", "Ministry of Finance Japan",
        "Asian Development Bank"
    ],
    "NGO": [
        "Greenpeace", "Red Cross", "Oxfam International", "World Wildlife Fund", "Doctors Without Borders",
        "Human Rights Watch", "Amnesty International", "Save the Children", "CARE International",
        "United Nations Foundation"
    ],
    "Corporation": [
        "ExxonMobil", "Tesla Inc.", "Amazon", "Microsoft Corporation", "Google (Alphabet Inc.)",
        "Apple Inc.", "Goldman Sachs", "JP Morgan Chase", "HSBC Holdings", "Deutsche Bank"
    ],
    "PEP": [
        "Vladimir Putin", "Joe Biden", "Narendra Modi", "Angela Merkel", "Boris Johnson",
        "Xi Jinping", "Emmanuel Macron", "Donald Trump", "Barack Obama", "Hillary Clinton"
    ]
}

#  Generate 500 unique names per category
labeled_data = []
for category, example_names in category_examples.items():
    for i in range(500):
        entity_name = random.choice(example_names) + f" {random.randint(10, 9999)}"
        labeled_data.append((entity_name, category))

#  Convert to DataFrame
df_labeled = pd.DataFrame(labeled_data, columns=["Entity Name", "Category"])

#  Save to CSV
df_labeled.to_csv("labeled_training_data.csv", index=False)
print(" Labeled training data saved as labeled_training_data.csv")
