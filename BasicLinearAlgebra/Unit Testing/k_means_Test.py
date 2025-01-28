import unittest
import numpy as np
from DataStructures.Vector import Vector
from Clustering import k_means

class Vector_Unit_Test(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)


    def test_select_random_group_representatives(self):

        k = 3
        n = np.random.randint(1,10)
        num_vectors = np.random.randint(10,50)
        N = [Vector(np.random.randint(0,100,n)) for x in range(num_vectors)]
        
        km = k_means.k_means(N, k)

        group_reps, assignment_candidates = km.select_random_group_representatives()

        is_found = False

        # Are any of the group representatives in the assignment candidates? Should be false as the groups are mutually exclusive
        for rep in group_reps:
            for candidate in assignment_candidates:
                if np.array_equal(rep.values, candidate.values.all):
                    is_found = True
                    break

        self.assertFalse(is_found)


        




    





    

unittest.main()