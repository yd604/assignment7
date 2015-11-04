# Author: Yihong Du

import numpy as np

# Question 1
# Write a module that creates the 2-D array without typing it explicitly
class create_array:
    def __init__(self):
        self.array = np.arange(1,16,1).reshape(3,5).transpose(1,0)

    # Q1a. Generate a new array containing the 2nd and 4th rows
    def picking_row(self):
        a = self.array[1:4:2]
        return a

    # Q1b. Generate a new array that contains the 2nd column
    def picking_column(self):
        b = self.array[:,1].reshape(5,1)
        return b

    # Q1c. Generate a new array that contains all the elements in the rectangular section between the coordinates [1,0] and [3,2]
    def picking_section(self):
        c = self.array[1:4]
        print type(c)
        return c

    # Q1d. Generate a new array that contains only elements with values that are between 3 and 11
    def picking_range(self):
        temp = self.array[self.array >= 3]
        d = temp[temp <= 11]
        print type(d)
        return d