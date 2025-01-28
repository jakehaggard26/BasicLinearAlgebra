import numpy as np
import copy
from DataStructures.Vector import Vector


class k_means:
    
    def __init__(self, vectors, k, iterations=100):
        # what we want to cluster
        self.N = vectors
        # the number of clusters
        self.k = k
        # cluster assignments; groups are 0 - k-1 so -1 is the default value to signal if a vector wasnt assigned a cluster
        self.c = np.full(len(self.N), -1)
        # Vector grouping indexes
        self.G = [set() for x in range(k)]
        # Group representatives
        self.z = list()
        # Number of iterations (Will stop early if the algorithm converges)
        self.iterations = iterations
        # Stores J Clust values to compare the current value to the value of the prior iteration
        self.j_clust_scores = []

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

        """
        Optimizes the group representatives by assigning vectors to their respective groups
        and then setting the group representatives to the centroid/mean of the vectors in the group.

        Returns:
            list: Returns a list of the optimized group representatives.
        """
       
       # Loop for each group in G & Assign vectors to the their grouping
        for i in range(len(self.G)):
            for j in range(len(self.c)):
                
                if self.c[j] == i:
                    self.G[i].add(j)

        # Set the group representatives to the centroid/mean of the vectors in the group
        for i in range(len(self.z)):
            self.z[i] = Vector(np.mean([self.N[j].values for j in self.G[i]], axis=0))

        return self.z
                

    def fit(self) -> list[set]:
        
        """
        Fits the k-means algorithm to the data by selecting random group representatives and then
        optimizing the group representatives by assigning vectors to their respective groups and then
        setting the group representatives to the centroid/mean of the vectors in the group.

        Returns:
            list[set]: Returns the grouping assignments of the vectors in N.
        """

        self.select_random_group_representatives()

        prior_j_clust = np.inf

        for i in range(self.iterations):

            j_clust = self.minimize_j_clust()
            print(j_clust)

            # Converges
            if round(j_clust, 16) == round(prior_j_clust, 16):
                print(f"Algorithm converged in {i + 1} iterations.")
                break

            # Store scores for comparison
            #self.j_clust_scores.append(j_clust)

            prior_j_clust = j_clust
            self.optimize_group_representatives()

        return self.c