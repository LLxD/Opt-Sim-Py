import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3*np.pi/5, 25)
y = np.sin(x) + np.random.random((25,))


def least_squares(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    return np.linalg.lstsq(A, y)[0]

m, c = least_squares(x, y)
plt.plot(x, y, 'o')
plt.plot(x, m*x + c, 'r')
plt.savefig('least_squares.png')