def suggest_investments(risk_profile):
    if risk_profile == 'high':
        return {"recommendations": ["Cryptocurrencies", "High-risk stocks", "Venture capital"]}
    elif risk_profile == 'medium':
        return {"recommendations": ["Balanced mutual funds", "Real estate", "Index funds"]}
    else:
        return {"recommendations": ["Bonds", "Dividend stocks", "Fixed deposits"]}