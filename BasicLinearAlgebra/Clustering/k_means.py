import numpy as np
import copy
from DataStructures.Vector import Vector


class k_means:
    
    def __init__(self, vectors, k):
        # what we want to cluster
        self.N = vectors
        # the number of clusters
        self.k = k
        # cluster assignments; groups are 0 - k-1 so -1 is the default value to signal if a vector wasnt assigned a cluster
        self.c = np.full(len(self.N), -1)
        # Vector grouping indexes
        self.G = [set()] * k
        # Group representatives
        self.z = list()
        # Stores J Clust values to compare the current value to the value of the prior iteration
        j_clust_scores = []

        pass

    def select_random_group_representatives(self):

        vectors_copy = copy.deepcopy(self.N)

        for i in range(self.k):
            rand = np.random.randint(0, len(vectors_copy))
            self.z.append(vectors_copy[rand])
            del vectors_copy[rand]

        # Returns group reps + candidates for assignment
        return self.z
    
    def minimize_j_clust(self) -> float:

        """
        Minimizes the J_clust value by assigning each vector in N to a group representative in v.
        Vectors are assigned to the group representative that is closest to them.

        Returns:
            float: Returns the optimized J_clust value.
        """
        
        j_clust = 0.0
        min_distance =  np.inf

        # Loop for each vector in N
        for i in range(len(self.N)):
            
            min_distance =  np.inf
            # Loop for each group representative in v
            for j in range(len(self.z)):
                # Calculate the distance between the vector and the group representative
                dist = (np.linalg.norm(self.N[i].values - self.z[j].values))**2

                # print(dist)
                # print(min_distance)
                # print()

                # If the distance is less than the current distance, update the distance and group assignment
                if dist < min_distance:
                    min_distance = dist
                    self.c[i] = j

            # Add the distance to the j_clust value
            j_clust += min_distance

        return j_clust / len(self.N)
    
    def optimize_group_representatives(self) -> list:
       
       # WIP

        return self.z
                