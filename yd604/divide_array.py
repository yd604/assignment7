# Author: Yihong Du

import numpy as np

# Question 2
# Divides each column element-wise with the array
def divide_array():   
    a = np.arange(25).reshape(5, 5)
    b = np.array([1., 5, 10, 15, 20])
    c = (a.transpose(1,0) / b).transpose(1,0)
    return c