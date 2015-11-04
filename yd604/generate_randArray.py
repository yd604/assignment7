# Author: Yihong Du

import numpy as np

# Question 3
# Write a module to generate a 10 x 3 array of random numbers in the range [0, 1)
def generate_randArray():
    randArray = np.random.rand(10,3)
    print 'The random array is \n', randArray
    print '\n'

    # pick the number closest to 0.5 for each row
    a = np.argsort(abs(randArray - 0.5))
    fancy_index = a[:,0]
    b = randArray[np.arange(0,10), fancy_index]
    print 'The 1-D array containing 10 values closest to 0.5 for each row is \n', b