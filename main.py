# K-Means Clustering

# Importing the Libraries
from sklearn.cluster import KMeans
import numpy as np

# Getting k value
k = int(input("Enter k value: " ))

# Loading data from txt file into a numpy array
lst = np.loadtxt('input.txt')

# Using KMeans algorithm and shaping the labels
kmeans = KMeans(n_clusters=k, random_state=0).fit(lst)
clusters = np.reshape(kmeans.labels_, (-1, 1))
final_result = np.hstack((lst, clusters + 1))

# Writing into the output txt file
a_file = open("output.txt", "w")
np.savetxt(a_file, final_result, fmt ='%.0f')
a_file.close()