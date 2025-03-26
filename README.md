# 🚀 AI-Driven Entity Intelligence Risk Analysis

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
The Entity Intelligence Risk Analysis Model automates the detection, verification, and risk scoring of entities (corporations, non-profits, shell companies, and financial intermediaries) involved in financial transactions. The model processes structured (CSV), unstructured (JSON & text), and publicly available news sources to assess risk levels based on ownership patterns, sanctions lists, and transaction behaviors.

## 🎥 Demo 
📹 [Video Demo](https://github.com/ewfx/aidel-code-302/tree/main/artifacts/demo)   

## ⚙️ What It Does
- Processes Structured & Unstructured Data (CSV, JSON, Text)
- Uses AI & NLP (BERT-based NER) to Extract Entity Relationships
- Cross-checks Entities Against Sanctions Lists (OFAC, World Bank, SEC Edgar)
- Assigns Risk Scores (High, Medium, Low) Based on Entity & Transaction Risk
- Generates Standardized Output in CSV/Excel Format
- REST API Integration for Frontend Dashboard

## 🛠️ How We Built It
- Extract Entities (Organizations, People, Locations) using BERT (NER).
- Identify Ownership Links 
- Risk Assessment (Sanctions List, Financial Crime Checks).
- Generate Structured Output (CSV) for further analysis.

## 🚧 Challenges We Faced
- Processing highly unstructured text data efficiently.
- Ensuring BERT’s NER model correctly detects organizations & people.
- Integrating real-time sanctions databases & news sources.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/your-repo.git](https://github.com/ewfx/aidel-code-302.git
   ```
2. Install dependencies  
   ```sh
   npm i  # for frontend
   pip install -r requirements.txt (for Python)   # for backend
   ```
3. Run the project  
   ```sh
   python src\main.py   # for frontend
   npm start            # for backend
   ```

## 🏗️ Tech Stack
- 🔹 Frontend: React, mUI
- 🔹 Backend: Python, Pandas, NumPy, Torch, sklearn, transformers, datasets, evaluate, json
- 🔹 Database: OFAC-SDN, Non-SDN, World Bank’s Debarred List

## 👥 Team
- **Code-302** - [GitHub](https://github.com/ewfx/aidel-code-302) 
