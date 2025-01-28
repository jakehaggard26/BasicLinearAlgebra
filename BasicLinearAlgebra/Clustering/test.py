from k_means import k_means
from DataStructures.Vector import Vector
import numpy as np

n = 5
num_vectors = 20
N = [Vector(np.random.randint(0,10,5)) for x in range(num_vectors)]
k = 3

km = k_means(N, k)

group_reps, assignment_candidates = km.select_random_group_representatives()

for i in range(len(N)):
    print(N[i].values)

print('----------------------------------------------------------------')

for i in range(len(assignment_candidates)):
    print(assignment_candidates[i].values)

print('----------------------------------------------------------------')

for i in range(len(group_reps)):
    print(group_reps[i].values)

km.minimize_j_clust()