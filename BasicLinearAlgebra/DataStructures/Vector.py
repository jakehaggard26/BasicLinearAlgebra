import numpy as np
import DataStructures.Vector as Vector
#import Vector as Vector
import copy

class Vector:

    def __init__(self, values: list[int|float]):
        
        self.values: np.array = np.asarray(values)
        pass

    
    def add(self, value: list[int | float]) -> Vector:

        """
        Adds a vector or scalar value to the current vector.
        If a vector is passed in, the corresponding entries of the two vectors are added to each other.
        If a scalar value is passed in, the scalar value is added to each entry in the vector.

        Returns:
            Vector: Returns the original vector with the value added to it.
        """

        if isinstance(value, Vector):
            for i in range(len(self.values)):
                self.values[i] += value.values[i]
        else:
            for i in range(len(self.values)):
                self.values[i] += value

        return self

    def subtract(self, value) -> Vector:

        """
        Subtracts a vector or scalar value from the current vector.
        If a vector is passed in, the corresponding entries of the two vectors are subtracted from each other.
        If a scalar value is passed in, the scalar value is subtracted from each entry in the vector.

        Returns:
            Vector: Returns the original vector with the value subtracted from it.
        """

        if isinstance(value, Vector):
            for i in range(len(self.values)):
                self.values[i] -= value.values[i]
        else:
            for i in range(len(self.values)):
                self.values[i] -= value

        return self

    def scale(self, scalar: int|float) -> Vector:

        """
        Scales the vector by a scalar value. This is done by multiplying each entry in the vector by the scalar value.

        Args:
            scalar (int | float): The scalar value to scale the vector by.

        Returns:
            Vector: The original vector scaled by the scalar value.
        """
        for i in range(len(self.values)):
            self.values[i] *= scalar

        return self

    def dot_product(self, vector: Vector) -> int | float:

        """
        For a given vector, calculate the dot product of the vector with another vector.
        The dot product is calculated by multiplying the corresponding entries of the two vectors and summing the result.

        Raises:
            ValueError: _description_

        Returns:
            int | float: Returns an integer or float value that represents the dot product.
        """

        dot_prod = 0

        if len(self.values) != len(vector.values):
            raise ValueError("Vectors are not the same size")

        for i in range(len(self.values)):
            dot_prod += (self.values[i] * vector.values[i])

        return dot_prod
    

    def euclidean_norm(self) -> int | float:

        """
        Calculates the Euclidean Norm of a vector. To do this we calculate the Dot Product of the
        vector with it self and take the square-root of the result. The Euclidean Norm can be interpretted as the magnitude of a vector.
        It's a geometric way to measure the distance of a vector

        Returns:
            int | float: The Euclidean Norm of the vector.
        """
    
        norm: int | float = 0

        norm = self.dot_product(self)
        norm = np.sqrt(norm)

        return norm
    
    def root_mean_square(self) -> int | float:

        """
        Calculates the Root Mean Square value of vector. It divides the norm of the vector the square-root of the 
        number of dimensions in the vector. This value tells us the typical value of an entry in the vector.

        Returns:
           int | float: The Root Mean Square value, the typical value of an entry in the vector.
        """

        rms: int | float = 0

        rms = self.euclidean_norm() / np.sqrt(len(self.values))

        return rms
    
    def distance(self, vector: Vector) -> int | float:

        """
        Calculates the Euclidean Distance of two vectors. It is calculated by finding the difference 
        of the two vectors and then getting the norm of the result.

        Returns:
            int | float: The Euclidean Distance.
        """
        
        distance: int | float = 0

        distance = ((self.subtract(vector)).euclidean_norm())

        return distance
    

    def sum(self) -> int | float:

        """
        Calculates the sum of all the entries in the vector.

        Returns:
            int | float: The sum of all the entries in the vector.
        """

        total: int | float = 0

        ones = Vector(np.full(len(self.values), 1))
        total = ones.dot_product(self)

        return total

    def average(self) -> int | float:

        """
        Calculates the average of all the entries in the vector.

        Returns:
            int | float: The average of the entries in the vector.
        """

        avg: int | float = 0

        denominator = Vector(np.full(len(self.values), 1 / len(self.values)))
        avg = denominator.dot_product(self)

        return avg
    
    def sum_of_squares(self) -> int | float:

        """
        Calculates the sum of the squares of all the entries in the vector. 
        This is done by calculating the dot product of the vector with itself.

        Returns:
            int | float: The sum of squares of the entries in the vector.
        """

        return self.dot_product(self)
    
    def weighted_sum(self, weights: Vector) -> int | float:

        """
        Calculates the weighted sum of the vector.
        This is done by calculating the dot product of the vector with the weights vector.

        Returns:
            int | float: The weighted sum of the vector.
        """
        
        return self.dot_product(weights)


    def demeaned_vector(self):

        """
        Calculates the demeaned vector of the vector.
        This is done by subtracting the average of the vector from each entry in the vector.

        Returns:
            Vector: The demeaned vector of the vector passed into the method.
        """

        avg_vector = Vector(np.full(len(self.values), self.average()))
        vector = copy.deepcopy(self)
        demeaned = vector.subtract(avg_vector)

        return demeaned
    
    def standard_deviation(self) -> int | float:

        """
        Calculates the standard deviation of the vector.
        This done by getting the demeaned vector,
        calculating the sum of the squares of the demeaned vector,
        dividing by the number of entries in the vector,
        and then taking the square root of the result.

        Returns:
            int | float: Returns the standard deviation of the vector.
        """
        
        std_dev: int | float = 0

        # Sum of squared demeaned vector entries
        std_dev = self.demeaned_vector()
        std_dev = std_dev.dot_product(std_dev)

        # Divide by n
        std_dev /= len(self.values)

        # Get the square root
        std_dev = np.sqrt(std_dev)

        return std_dev
    
    def angle_between_vectors(self, vector: Vector) -> int | float:

        """
        Given two vectors, calculate the angle between them.
        This is done by calculating the dot product of the two vectors,
        dividing by the product of the Euclidean Norm of the two vectors,
        and then taking the arccos of the result.

        Returns:
            int | float: The angle between the two vectors in radians.
        """
        
        angle = 0

        angle = np.arccos(self.dot_product(vector) / (self.euclidean_norm() * vector.euclidean_norm()))

        return angle
    
    def calculate_z_scores(self) -> Vector:

        """
        Given a vector, calculate the Z-scores of the vector.
        This is done by getting the demeaned vector,
        scaling the demeaned vector by the inverse of the standard deviation.

        Returns:
            Vector: Returns a vector of the Z-scores of the original vector.
        """
        
        demeaned_vector = self.demeaned_vector()
        inv_std_dev = ( 1 / self.standard_deviation())
        z = demeaned_vector.scale(inv_std_dev)

        return z

    def correlation_coefficient(self, vector: Vector) -> int | float:
        # WIP: Is not accurate :(
        corr_coef: int | float = 0
        
        # corr_coef = (self.demeaned_vector().dot_product(vector.demeaned_vector())
        #                 / (self.demeaned_vector().euclidean_norm() * vector.demeaned_vector().euclidean_norm())
        #             )

        u = (self.demeaned_vector().scale( 1 / self.standard_deviation())) 
        v = (vector.demeaned_vector().scale(1 / vector.standard_deviation())) 

        print(self.values)
        print(u.values)
        print(vector.values)
        print(v.values)

        corr_coef = u.dot_product(v) / len(vector.values)

        return corr_coef
