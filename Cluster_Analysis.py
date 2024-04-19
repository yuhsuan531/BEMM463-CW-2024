import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generate synthetic data
np.random.seed(0)
n_samples = 500
n_features = 5  # Number of variables
X, _ = make_blobs(n_samples=n_samples, centers=5, n_features=n_features)

# Perform KMeans clustering
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Visualize the clusters
plt.figure(figsize=(8, 6))

# Choose two dimensions for visualization (e.g., age and price)
x_dimension = 0
y_dimension = 1

plt.scatter(X[:, x_dimension], X[:, y_dimension], c=y_kmeans, cmap='viridis', s=50, alpha=0.5)
centers = kmeans.cluster_centers_
plt.scatter(centers[:, x_dimension], centers[:, y_dimension], c='red', s=200, alpha=0.8, marker='X')
plt.xlabel('Age')
plt.ylabel('Price')
plt.title('Cluster Analysis of Jewelry Market')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()
