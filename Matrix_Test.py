import unittest
import numpy as np
from DataStructures.Matrix import Matrix

class Matrix_Unit_Test(unittest.TestCase):

    def __init__(self, methodName = "runTest", sample_size: int = 5):
        super().__init__(methodName)

        self.sample_one = np.random.random_sample(sample_size)
        self.sample_two = np.random.random_sample(sample_size)

    
    def test_Matrix_creation(self):

        solution: np.array = np.random.random_sample(10)
        mat1 = Matrix()

        mat1.matrix = [
            np.array([1, 2, 3, 4]),
            np.array([5, 6, 7, 8])
        ]
   

        print(mat1.__str__())

        # for i in range(len(vector.values)):
        #     self.assertEqual(vector.values[i], solution[i])



    
# Runs Unit-Test
unittest.main()