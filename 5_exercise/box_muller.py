# implement the Box-Muller method to generate random numbers from a normal distribution

import numpy as np
import matplotlib.pyplot as plt

# generate random numbers from a uniform distribution

N = 100000
x = np.random.uniform(0, 1, N)
y = np.random.uniform(0, 1, N)

# transform them to random numbers from a normal distribution

r = np.sqrt(-2 * np.log(x))
theta = 2 * np.pi * y
z1 = r * np.cos(theta)
z2 = r * np.sin(theta)

# plot the results

plt.hist(z1, bins=100, density=True, label='z1')
plt.hist(z2, bins=100, density=True, label='z2')

# save the figure inside the folder 5_exercise

plt.savefig('box_muller.png')
