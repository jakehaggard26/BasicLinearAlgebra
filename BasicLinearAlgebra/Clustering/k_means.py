import numpy as np
import copy
from DataStructures.Vector import Vector


class k_means:
    
    def __init__(self, vectors, k):
        # what we want to cluster
        self.N = vectors
        # the number of clusters
        self.k = k
        # cluster assignments; groups are 1 - k so 0 is the default value to signal if a vector wasnt assigned a cluster
        self.c = np.full(len(self.N), 0)
        # Vector grouping indexes
        self.G = [set()] * k
        # Group representatives
        self.v = list()
        # Stores J Clust values to compare the current value to the value of the prior iteration
        j_clust_scores = []

        pass

    def select_random_group_representatives(self):

        vectors_copy = copy.deepcopy(self.N)

        for i in range(self.k):
            rand = np.random.randint(len(self.N))

            self.v.append(vectors_copy[rand])
            del vectors_copy[rand]

        # Returns group reps + candidates for assignment
        return [self.v, vectors_copy]