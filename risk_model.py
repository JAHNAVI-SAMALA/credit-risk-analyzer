def calculate_risk(income, credit_score, debt, savings, late_payments):
    score = 0

    # Credit Score
    if credit_score >= 750:
        score += 0
    elif credit_score >= 700:
        score += 1
    else:
        score += 2

    # Debt-to-Income Ratio
    dti = debt / income
    if dti < 0.3:
        score += 0
    elif dti < 0.6:
        score += 1
    else:
        score += 2

    # Savings
    if savings > 100000:
        score += 0
    elif savings > 50000:
        score += 1
    else:
        score += 2

    # Late Payments
    score += late_payments

    # Final Risk Classification
    if score <= 2:
        return "Low Risk", score
    elif score <= 5:
        return "Medium Risk", score
    else:
        return "High Risk", score