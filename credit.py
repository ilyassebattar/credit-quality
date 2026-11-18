def calculate_risk(income, debt, age):
    """Calcule le niveau de risque à partir du revenu et de la dette."""
    if income <= 0:
        return -1

    ratio = debt / income

    if ratio > 0.6:
        return "HIGH"
    if ratio > 0.3:
        return "MEDIUM"
    return "LOW"