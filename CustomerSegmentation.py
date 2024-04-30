import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load customer data
customers_df = pd.read_csv('Customers.csv')  

# Select features for clustering
features = ['Age', 'Annual_Income', 'Spending_Score']
X = customers_df[features]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

#ELBOW CURVE
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Based on the elbow curve, choosing optimal number of clusters
n_clusters = 5

#K_MEANS CLUSTERING
kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
kmeans.fit(X_scaled)


customers_df['Cluster'] = kmeans.labels_

# Visualization
plt.figure(figsize=(10, 6))
for cluster in range(n_clusters):
    cluster_data = customers_df[customers_df['Cluster'] == cluster]
    plt.scatter(cluster_data['Annual_Income'], cluster_data['Spending_Score'], label=f'Cluster {cluster}')

plt.scatter(kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 2], s=300, c='red', label='Centroids')
plt.title('Customer Segmentation')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()
