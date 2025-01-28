from k_means import k_means
from DataStructures.Vector import Vector
import numpy as np

n = 3
num_vectors = 15
N = [Vector(np.random.randint(-100,100,n)) for x in range(num_vectors)]
k = 4

km = k_means(N, k)
iterations = 3

gr = km.select_random_group_representatives()

for rep in gr:
    print(rep.values)

print(km.c)
for i in range(iterations):
    print(km.minimize_j_clust())
    km.optimize_group_representatives()
    print(km.c)
