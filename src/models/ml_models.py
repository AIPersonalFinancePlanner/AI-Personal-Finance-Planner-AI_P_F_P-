from sklearn.cluster import KMeans

class SpendingCluster:
    def __init__(self):
        self.model = KMeans(n_clusters=3)

    def cluster_spending(self, amounts):
        return self.model.fit_predict(amounts)

    def generate_advice(self, df, income):
        advice = []
        if df['amount'].sum() > income:
            advice.append("Your expenses exceed your income. Consider cost-cutting or income enhancement.")
        else:
            advice.append("You're within your budget. Good job!")

        for cluster in df['cluster'].unique():
            cluster_data = df[df['cluster'] == cluster]
            categories = cluster_data['category'].unique()
            advice.append(f"Cluster {cluster}: Frequent spending in {', '.join(categories)} could be optimized.")

        return advice