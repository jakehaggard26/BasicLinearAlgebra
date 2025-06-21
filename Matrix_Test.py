import unittest
import numpy as np
from DataStructures.Matrix import Matrix
from DataStructures.Vector import Vector

class Matrix_Unit_Test(unittest.TestCase):

    def __init__(self, methodName = "runTest", sample_size: int = 5):
        super().__init__(methodName)

        self.sample_one = np.random.randint(1, 10, sample_size)
        self.sample_two = np.random.randint(1, 10, sample_size)
    
    def test_Matrix_empty_creation(self):
        matrix_one = Matrix()

        self.assertIs(matrix_one.matrix, None)




    def test_matrix_creation(self):
        matrix_one = Matrix([
            Vector(self.sample_one),
            Vector(self.sample_two)
        ])

        rand_num_matrix = [self.sample_one, self.sample_two]
        
        for i in range(matrix_one.rows):
            for j in range(matrix_one.columns):

                self.assertEqual(matrix_one.matrix[i].values[j], rand_num_matrix[i][j])

    
    def test_matrix_modification(self):
        matrix_one = Matrix()

        rand_num_matrix = [self.sample_one, self.sample_two]

        matrix_one.matrix = [
            Vector(self.sample_one),
            Vector(self.sample_two)
        ]

        # Change value in row 2, column 1 to -1
        matrix_one.matrix[1].values[0] = -1
        rand_num_matrix[1][0] = -1
        
        for i in range(matrix_one.rows):
            for j in range(matrix_one.columns):
                self.assertEqual(matrix_one.matrix[i].values[j], rand_num_matrix[i][j])



    
# Runs Unit-Test
unittest.main()