import numpy as np
import matplotlib.pyplot as plt

def dfdt(f, t):
    h = 2**(-26)
    return (f(t+h) - f(t))/(2*h)

t = np.linspace(0, 2*np.pi, 100)
fun = lambda x: np.sin(x)
plt.plot(t, fun(t), 'b', label='sin(x)')
plt.plot(t, dfdt(fun, t), 'r', label='derivative')
plt.legend()
plt.savefig('deriv.png')