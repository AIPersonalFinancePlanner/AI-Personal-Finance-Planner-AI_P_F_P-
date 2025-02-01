import pandas as pd
from models.ml_models import SpendingCluster

def analyze_budget(transactions, income):
    df = pd.DataFrame(transactions)
    df['date'] = pd.to_datetime(df['date'])
    
    # Use ML model for clustering
    model = SpendingCluster()
    df['cluster'] = model.cluster_spending(df['amount'].values.reshape(-1, 1))
    
    advice = model.generate_advice(df, income)
    return {
        "analysis": advice,
        "categories": df['category'].value_counts().to_dict()
    }