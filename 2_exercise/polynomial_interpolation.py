import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 32)
y = np.cos(x)

def polynomial_interpolation(x, y, n):
    A = np.zeros((len(x), n))
    for i in range(len(x)):
        for j in range(n):
            A[i, j] = x[i]**j
    return np.linalg.lstsq(A, y)[0]

def main():
    for n in range(2, 6):
        coeffs = polynomial_interpolation(x, y, n)
        mean_squared_error = np.mean((np.dot(np.vander(x, n), coeffs) - y)**2)
        print(coeffs, mean_squared_error)
        plt.plot(x, y, 'b')
        #save all of them into the same figure with different colors
        plt.plot(x, np.dot(np.vander(x, n), coeffs), c=np.random.rand(3,))
        plt.savefig('polynomial_interpolation.png')
        
        
if __name__ == '__main__':
    main()