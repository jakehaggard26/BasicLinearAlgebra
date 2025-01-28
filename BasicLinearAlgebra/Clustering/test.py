from k_means import k_means
from DataStructures.Vector import Vector
import numpy as np

n = 8
num_vectors = 15000
#N = [Vector(np.random.randint(-10,10,n)) for x in range(num_vectors)]
N = [
    # Age, Income, Credit Score
    Vector([26, 36500, 427]),
    Vector([29, 45000, 562]),
    Vector([42, 98000, 697]),
    Vector([27, 58000, 625]),
    Vector([45, 136500, 654]),
    Vector([24, 22500, 459]),
    
    Vector([48, 125000, 671]),
    Vector([49, 97500, 725])
]
k = 2


iterations = 50
km = k_means(N, k, iterations)

km.fit()

print(km.c)