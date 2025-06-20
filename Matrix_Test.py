import unittest
import numpy as np
from DataStructures.Matrix import Matrix

class Matrix_Unit_Test(unittest.TestCase):

    def __init__(self, methodName = "runTest", sample_size: int = 5):
        super().__init__(methodName)

        self.sample_one = np.random.random_sample(sample_size)
        self.sample_two = np.random.random_sample(sample_size)

    
    def test_Matrix_creation(self):

        mat1 = Matrix()
        
        rand_nums1: np.array = np.random.randint(1,10,5)
        rand_nums2: np.array = np.random.randint(1,10,5)

        rand_num_matrix = [rand_nums1, rand_nums2]

        mat1.matrix = [
            rand_nums1,
            rand_nums2
        ]
   

        print(mat1.__str__())

        # for i in range(len(vector.values)):
        #     self.assertEqual(vector.values[i], solution[i])

        for i in range(mat1.rows):
            for j in range(mat1.columns):
                self.assertEqual(mat1.matrix[i][j], rand_num_matrix[i][j])



    
# Runs Unit-Test
unittest.main()