# Author: Yihong Du

import numpy as np
import matplotlib.pyplot as plt

# Question 4
# Write a module that computes the Mandelbrot fractal using the Mandelbrot iteration
class mandelbrot:

    def __init__(self, grid_num):
        self.N_max = 50
        self.some_threshold = 50

        # Constructing a grid of 1000 uniformly distributed values in the range [-2, 1] x [-1.5, 1.5]
        self.x_grid = np.linspace(-2, 1, grid_num)
        self.y_grid = np.linspace(-1.5, 1.5, grid_num)
        self.x, self.y = np.meshgrid(self.x_grid, self.y_grid)
        self.c = self.x + 1j * self.y
        self.z = self.c

        # Mandelbrot iteration
    def mandelbrot_iter(self):
        for v in range(self.N_max):
            self.z = self.z**2 + self.c
        return self.z
        
        # Form a 2-D boolean mask indicating which points are in the set
    def form_mask(self):
        mask = (abs(self.z) < self.some_threshold)

        # Save the result to an image
        plt.imshow(mask, extent=[-2, 1, -1.5, 1.5])
        plt.gray()
        plt.savefig('mandelbrot.png')