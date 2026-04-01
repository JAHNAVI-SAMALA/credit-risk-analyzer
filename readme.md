# 💳 Credit Risk Analyzer

## 📌 Overview
The Credit Risk Analyzer is a web-based application that evaluates the likelihood of a borrower defaulting on a loan using key financial indicators. This project simulates a simplified version of credit risk assessment used in financial institutions.

---

## 🚀 Features
- 📊 Risk classification (Low / Medium / High)
- 🧮 Rule-based risk scoring model
- 📈 Graph visualization (Risk Score vs Debt)
- 💡 Dynamic insights based on financial profile
- 🌐 Interactive web interface using Flask

---

## 🧠 Risk Factors Considered
- Annual Income  
- Credit Score  
- Debt-to-Income Ratio (DTI)  
- Savings  
- Late Payments  

---

## ⚙️ Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS  
- **Visualization:** Matplotlib  

---

## 🧮 How It Works
The model assigns a risk score based on:
- Creditworthiness (credit score)
- Debt burden (Debt-to-Income ratio)
- Financial stability (savings)
- Repayment behavior (late payments)

### Risk Levels:
- **Low Risk** → Strong financial profile  
- **Medium Risk** → Moderate financial risk  
- **High Risk** → High probability of default  

---

## 📊 Visualization
The application generates a graph showing how the risk score changes with increasing debt, helping users understand risk sensitivity.

---

## 💡 Insights
The system provides dynamic insights based on the user's financial data, helping interpret the risk level in a practical way.

---

## 🖥️ How to Run

### 1. Clone the repository

**git clone https://github.com/JAHNAVI-SAMALA/credit-risk-analyzer.git**
cd credit-risk-analyzer

### 2. Install dependencies
pip install flask matplotlib

### 3. Run the application
python app.py

### 4. Open in browser
http://127.0.0.1:5000

---

### 📌 Example Use Case

A user enters financial details such as income, debt, and credit score.
**The system:**

- Calculates a risk score
- Classifies the borrower
- Displays a graph of risk vs debt
- Provides an insight explaining the result

---

### ⚠️ Limitations
- Rule-based model (not machine learning)
- Simplified assumptions
- Does not reflect real-world banking systems

---

## 🔮 Future Improvements
- Integrate machine learning models for prediction
- Use real-world financial datasets
- Add user authentication and history tracking
- Deploy as a live web application

---

## 👤 Author
**Jahnavi Samala – BTech CSE Student**
---

## ⭐ Acknowledgment

This project was inspired by a credit risk assessment simulation from Goldman Sachs (Forage Virtual Experience Program).
