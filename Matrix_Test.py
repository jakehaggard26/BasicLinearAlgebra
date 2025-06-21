import unittest
import numpy as np
from DataStructures.Matrix import Matrix

class Matrix_Unit_Test(unittest.TestCase):

    def __init__(self, methodName = "runTest", sample_size: int = 5):
        super().__init__(methodName)

        self.sample_one = np.random.randint(1, 10, sample_size)
        self.sample_two = np.random.randint(1, 10, sample_size)
    
    def test_Matrix_creation(self):

        matrix_one = Matrix()

        rand_num_matrix = [self.sample_one, self.sample_two]

        matrix_one.matrix = [
            self.sample_one,
            self.sample_two
        ]
        print(matrix_one.__str__())
        for i in range(matrix_one.rows):
            for j in range(matrix_one.columns):
                self.assertEqual(matrix_one.matrix[i][j], rand_num_matrix[i][j])



    
# Runs Unit-Test
unittest.main()