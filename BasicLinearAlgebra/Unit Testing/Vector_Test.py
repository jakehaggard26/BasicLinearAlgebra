import unittest
import numpy as np
from DataStructures.Vector import Vector
from Clustering import k_means

class Vector_Unit_Test(unittest.TestCase):

    def __init__(self, methodName = "runTest", sample_size: int = 5):
        super().__init__(methodName)

        self.sample_one = np.random.random_sample(sample_size)
        self.sample_two = np.random.random_sample(sample_size)

    def test_vector_creation(self):

        solution: np.array = np.random.random_sample(10)
        vector = Vector(solution)

        for i in range(len(vector.values)):
            self.assertEqual(vector.values[i], solution[i])

    
    def test_vector_add(self):

        samples_added: np.array = self.sample_one + self.sample_two
        constant = np.random.random(1)

        vector_one = Vector(self.sample_one)
        vector_two = Vector(self.sample_two)

        vector_one.add(vector_two)
        
        for i in range(len(vector_one.values)):
            self.assertEqual(vector_one.values[i], samples_added[i])

        
        samples_added = self.sample_one + constant
        vector_one.add(constant)
        
        for i in range(len(vector_one.values)):
            self.assertEqual(vector_one.values[i], samples_added[i])

    
    def test_vector_subtract(self):

        samples_subtracted: np.array = self.sample_one - self.sample_two

        constant = np.random.random(1)
        vector_one = Vector(self.sample_one)
        vector_two = Vector(self.sample_two)

        vector_one.subtract(vector_two)

        for i in range(len(vector_one.values)):
            self.assertEqual(vector_one.values[i], samples_subtracted[i])

        
        samples_subtracted = self.sample_one - constant
        vector_one.subtract(constant)
        
        for i in range(len(vector_one.values)):
            self.assertEqual(vector_one.values[i], samples_subtracted[i])

    
    def test_vector_scale(self):

        scalar: int|float = 0.75
        samples_scaled = self.sample_one * scalar

        vector_one = Vector(self.sample_one)
        vector_one.scale(scalar)

        for i in range(len(vector_one.values)):
            self.assertEqual(vector_one.values[i], samples_scaled[i])

    
    def test_vector_dot_product(self):

        vector_one = Vector(self.sample_one)
        vector_two = Vector(self.sample_two)

        samples_dot_product: float|int = np.dot(self.sample_one, self.sample_two)

        self.assertEqual(vector_one.dot_product(vector_two), samples_dot_product)


    def test_vector_euclidean_norm(self):
        
        vector_one = Vector(self.sample_one)

        sample_norm = np.linalg.norm(self.sample_one)

        self.assertEqual(vector_one.euclidean_norm(), sample_norm)

    def test_root_mean_square(self):

        vector_one = Vector(self.sample_one)

        sample_rms = np.sqrt(np.mean(self.sample_one**2))

        self.assertEqual(round(vector_one.root_mean_square(), 8), round(sample_rms, 8))

    def test_distance(self):

        vector_one = Vector(self.sample_one)
        vector_two = Vector(self.sample_two)

        sample_distance = np.linalg.norm(vector_one.values - vector_two.values)

        self.assertEqual(round(vector_one.distance(vector_two), 8), round(sample_distance, 8))

    def test_sum(self):
        vector_one = Vector(self.sample_one)

        sample_sum = np.sum(vector_one.values)

        self.assertEqual(round(vector_one.sum(), 8), round(sample_sum, 8))

    def test_sum_of_squares(self):
        vector_one = Vector(self.sample_one)

        sample_sum = np.sum(vector_one.values**2)

        self.assertEqual(round(vector_one.dot_product(vector_one), 8), round(sample_sum, 8))

    def test_average(self):
        vector_one = Vector(self.sample_one)

        sample_average = np.average(vector_one.values)

        self.assertEqual(round(vector_one.average(), 8), round(sample_average, 8))

    def test_demeaned_vector(self):
        vector_one = Vector(self.sample_one)
        sample_demean = self.sample_one - np.average(self.sample_one)

        for i in range(len(vector_one.demeaned_vector().values)):
            self.assertEqual(round(vector_one.demeaned_vector().values[i], 8), round(sample_demean[i], 8))



    def test_standard_deviation(self):
        vector_one = Vector(self.sample_one)

        sample_std_dev = np.std(vector_one.values)

        self.assertEqual(round(vector_one.standard_deviation(), 8), round(sample_std_dev, 8))


    def test_angle_between_vectors(self):

        vector_one = Vector(self.sample_one)
        vector_two = Vector(self.sample_two)
        
        dot_product = np.dot(self.sample_one, self.sample_two)
        
        # Compute the magnitudes of vectors a and b
        mag_a = np.linalg.norm(self.sample_one)
        mag_b = np.linalg.norm(self.sample_two)
        
        # Compute the cosine of the angle
        cos_theta = dot_product / (mag_a * mag_b)
        
        # Ensure cos_theta is within the valid range of arccos [-1, 1] due to numerical precision
        cos_theta = np.clip(cos_theta, -1.0, 1.0)
        
        # Compute the angle in radians
        sample_angle_rad = np.arccos(cos_theta)

        self.assertEqual(round(vector_one.angle_between_vectors(vector_two), 8), round(sample_angle_rad, 8))


    def test_z_score(self):

        vector_one = Vector(self.sample_one)
        
        sample_z_scores = (self.sample_one - self.sample_one.mean()) / self.sample_one.std()
        z_scores = vector_one.calculate_z_scores()

        for i in range(len(vector_one.values)):
            self.assertEqual(round(z_scores.values[i], 8), round(sample_z_scores[i], 8))






    # def test_correlation_coefficient(self):

    #     vector_one = Vector(self.sample_one)
    #     vector_two = Vector(self.sample_two)

    #     sample_correlation_coefficient = np.corrcoef(vector_one.values, vector_two.values)

    #     self.assertEqual(round(vector_one.angle_between_vectors(vector_one.correlation_coefficient(vector_two)), 8), round(sample_correlation_coefficient, 8))

    

unittest.main()