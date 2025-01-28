from k_means import k_means
from DataStructures.Vector import Vector
import numpy as np

n = 8
num_vectors = 15000
N = [Vector(np.random.randint(-10,10,n)) for x in range(num_vectors)]
k = 4


iterations = 50
km = k_means(N, k, iterations)

km.fit()

print(km.c)