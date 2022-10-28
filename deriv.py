import numpy as np
import matplotlib.pyplot as plt

def dfdt(f, t):
    h = 2**(-26)
    return (f(t+h) - f(t))/(2*h)


# create a function to get the second derivative
def d2fdt2(f, t):
    h = 2**(-26)
    return (f(t+h) - 2*f(t) + f(t-h))/(h**2)

t = np.linspace(0, 2*np.pi, 100)
fun = lambda x: np.sin(x)
plt.plot(t, fun(t), 'b', label='sin(x)')
plt.plot(t, dfdt(fun, t), 'r', label='derivative')
plt.legend()
plt.savefig('deriv.png')

plt.plot(t, d2fdt2(fun, t), 'g', label='second derivative')
plt.legend()
plt.savefig('deriv2.png')