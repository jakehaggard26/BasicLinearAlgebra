from DataStructures.Vector import Vector
import numpy as np
from scipy.stats import pearsonr
import copy

v_one = Vector([10,20,40,80])
v_two = Vector([1.665,2.864,3.7,4.0012154])
v_random = Vector(np.random.randint(1,10,4))



r = v_one.correlation_coefficient(v_two)



print(r)
print(pearsonr(v_one.values, v_two.values))
print(np.corrcoef(v_one.values, v_two.values))