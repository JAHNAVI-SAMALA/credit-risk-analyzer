from flask import Flask, render_template, request
from risk_model import calculate_risk
import matplotlib.pyplot as plt
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    risk = None
    score = None
    graph_path = None
    insight = None

    if request.method == 'POST':
        income = float(request.form['income'])
        credit_score = int(request.form['credit_score'])
        debt = float(request.form['debt'])
        savings = float(request.form['savings'])
        late_payments = int(request.form['late_payments'])

        risk, score = calculate_risk(income, credit_score, debt, savings, late_payments)

        # Generate dynamic debt values
        debts = list(range(0, int(debt) + 50000, 10000))
        scores = []

        for d in debts:
            _, s = calculate_risk(income, credit_score, d, savings, late_payments)
            scores.append(s)

        # 🔥 Improved Graph
        plt.figure(figsize=(6,4))
        plt.plot(debts, scores, marker='o')
        plt.title("Risk Score vs Debt")
        plt.xlabel("Debt")
        plt.ylabel("Risk Score")
        plt.grid()

        # Unique filename (IMPORTANT)
        graph_path = f"static/graph_{int(time.time())}.png"
        plt.savefig(graph_path, bbox_inches='tight')
        plt.close()
        insight = None

        if risk:
            if risk == "Low Risk":
                insight = "Strong financial profile with low default probability."
            elif risk == "Medium Risk":
                insight = "Moderate risk due to debt or repayment behavior."
            else:
                insight = "High risk driven by high debt and/or poor credit behavior."

    return render_template(
        'index.html',
        risk=risk,
        score=score,
        graph=graph_path,
        insight=insight
)
    
if __name__ == '__main__':
    app.run(debug=True)