from Clustering.k_means import k_means
from DataStructures.Vector import Vector
import numpy as np

# number of elements in a vector
n = 8

# number of vectors
num_vectors = 15000
#N = [Vector(np.random.randint(-10,10,n)) for x in range(num_vectors)]
N = [
    # Age, Income, Credit Score
    Vector([26, 36500, 427]), # "Poor" person
    Vector([29, 45000, 562]), # "Poor" person
    Vector([42, 98000, 697]), # "Rich" person
    Vector([27, 58000, 625]), # "Poor" person
    Vector([45, 136500, 654]), # "Rich" person
    Vector([24, 22500, 459]), # "Poor" person
    
    Vector([48, 125000, 671]), # "Rich" person
    Vector([49, 97500, 725]), # "Rich" person

    Vector([56, 1250000, 750]), # "Super Rich" person
    Vector([59, 1500000, 750]) # "Super Rich" person
]

# number of clusters
k = 3

iterations = 50
km = k_means(N, k, iterations)

km.fit()

print(km.c)