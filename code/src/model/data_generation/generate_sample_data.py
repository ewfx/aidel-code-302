import pandas as pd
import random
from faker import Faker
from datetime import datetime
import json

fake = Faker()

# ✅ Realistic High-Risk Entities (From Sanctions Lists & Financial Crimes Databases)
high_risk_entities = [
    "Gazprom", "Rostec", "North Korea Trading Corporation",
    "Vladimir Putin", "Nicolas Maduro", "Shell Holdings Ltd",
    "ABC Offshore Services", "Crypto Exchange Ltd", "Hawala Network Inc"
]

# ✅ Realistic Government Organizations, NGOs, Corporations, and PEPs
entity_names = [
    "United Nations", "World Health Organization", "Red Cross",
    "Tesla Inc.", "Goldman Sachs", "HSBC Holdings", "JP Morgan Chase",
    "Shell Trading Ltd", "Greenpeace", "ExxonMobil", "BlackRock",
    "Panama Offshore Holdings", "Rothschild & Co", "Oxfam International"
]

# ✅ Realistic Banks
banks = ["Swiss National Bank", "Cayman National Bank", "Deutsche Bank", "HSBC", "JP Morgan Chase"]

# ✅ High-Risk & Common Financial Hubs
countries = ["Switzerland", "Cayman Islands", "Germany", "USA", "UK", "Panama", "British Virgin Islands", "Russia", "China"]

# ✅ Currencies & Transaction Types
currencies = ["USD", "EUR", "GBP", "BTC", "ETH"]
transaction_types = ["Wire Transfer", "SWIFT", "Cryptocurrency", "Cheque"]

# ✅ Transaction Statuses
statuses = ["Completed", "Pending", "Rejected", "Under Review"]

# ✅ Additional Data for Risk Analysis
ip_addresses = ["192.168.29.183", "203.45.67.22", "180.76.76.50", "102.56.12.34"]
risk_flags = ["OFAC Sanctions Match", "High-Risk Country", "Politically Exposed Person (PEP)", "No Red Flags"]

# ✅ Generate Sample Structured Data
structured_data = []
for i in range(100):  # Generate 100 transactions
    structured_data.append([
        f"TXN{i+1:04d}",  # Unique Transaction ID
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Date
        random.choice(high_risk_entities + entity_names),  # Sender Name
        random.choice(countries),  # Sender Country
        random.choice(banks),  # Sender Bank
        random.choice(entity_names),  # Receiver Name
        random.choice(countries),  # Receiver Country
        random.choice(banks),  # Receiver Bank
        random.choice(transaction_types),  # Transaction Details
        f"${random.randint(10000, 5000000):,}",  # Amount
        random.choice(statuses)  # Status
    ])

# ✅ Create DataFrame & Save as CSV
df_structured = pd.DataFrame(structured_data, columns=[
    "Transaction ID", "Date", "Sender Name", "Sender Country", "Sender Bank",
    "Receiver Name", "Receiver Country", "Receiver Bank", "Transaction Details",
    "Amount", "Status"
])
df_structured.to_csv("structured_data.csv", index=False)
print("Structured data saved to structured_data.csv")

# ✅ Function to Generate Realistic Unstructured Data
def generate_transaction():
    sender = random.choice(high_risk_entities + entity_names)
    receiver = random.choice(entity_names)
    sender_country = random.choice(countries)
    receiver_country = random.choice(countries)
    sender_bank = random.choice(banks)
    receiver_bank = random.choice(banks)
    amount = f"${random.randint(10000, 5000000):,}"
    currency = random.choice(currencies)
    transaction_type = random.choice(transaction_types)
    status = random.choice(statuses)
    risk_flag = random.choice(risk_flags)
    ip_address = random.choice(ip_addresses)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transaction = {
        "Transaction ID": f"TXN-{random.randint(1000, 9999)}-{random.randint(100, 999)}",
        "Date": timestamp,
        "Sender": {
            "Name": sender,
            "Country": sender_country,
            "Bank": sender_bank,
            "Account": f"IBAN {random.randint(100000, 999999)} {random.randint(100000, 999999)} {random.randint(100000, 999999)}",
            "Address": f"{random.randint(100, 999)} Rue de {random.choice(['Marche', 'Finance', 'Commerce'])}, {sender_country}",
            "Notes": f"{random.choice(['Consulting Fee', 'Project Investment', 'Charitable Donation', 'Loan Repayment'])}"
        },
        "Receiver": {
            "Name": receiver,
            "Country": receiver_country,
            "Bank": receiver_bank,
            "Account": f"IBAN {random.randint(100000, 999999)} {random.randint(100000, 999999)} {random.randint(100000, 999999)}",
            "Address": f"{random.randint(100, 999)} Main Street, {receiver_country}",
            "Tax ID": f"TX-{random.randint(1000, 9999)}"
        },
        "Amount": f"{amount} {currency}",
        "Transaction Type": transaction_type,
        "Status": status,
        "Compliance Check": risk_flag,
        "IP Address": ip_address,
        "Additional Notes": [
            f"Invoice matched with contract ref {random.randint(100, 999)}-{random.randint(1000, 9999)}",
            f"Sender IP {ip_address} detected using VPN exit mode in {random.choice(countries)}",
            f"Regulatory screening pending for further due diligence"
        ]
    }
    return transaction

# ✅ Generate Unstructured Data and Save as JSON
def generate_unstructured_data(file_name="unstructured_transactions.json", num_records=100):
    data = [generate_transaction() for _ in range(num_records)]
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Generated {num_records} unstructured transactions and saved to {file_name}")

# ✅ Run the Script
generate_unstructured_data()
