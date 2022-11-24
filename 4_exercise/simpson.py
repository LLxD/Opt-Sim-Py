# https://en.wikipedia.org/wiki/Simpson%27s_rule

from math import log, sin, pi, sqrt
from scipy import integrate


def simpson_1_3(f, a, b):
    return (b-a)/6*(f(a) + 4*f((a+b)/2) + f(b))

def simpson_3_8(f, a, b):
    return (b-a)/8*(f(a) + 3*f((2*a+b)/3) + 3*f((a+2*b)/3) + f(b))

def gaussian_quadrature(f, a, b):
    return (b-a)/2*(f((b-a)/2*sqrt(1/3) + (a+b)/2) + f(-(b-a)/2*sqrt(1/3) + (a+b)/2))



print("case 1")
f = lambda x: x**2 + 1
lim = [0, 2]
resp = 14/3
calc = simpson_1_3(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = simpson_3_8(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = gaussian_quadrature(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = integrate.quad(f, *lim)[0]
print(calc, "error:", abs(resp-calc))

print("case 2")
f = lambda x: (2*x**5 - x + 3)/x**2
lim = [1, 2]
resp = 9 - log(2)
calc = simpson_1_3(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = simpson_3_8(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = gaussian_quadrature(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = integrate.quad(f, *lim)[0]
print(calc, "error:", abs(resp-calc))

print("case 3")
f = lambda x: x**0.5*(x-2)
lim = [0, 4]
resp = 32/15
calc = simpson_1_3(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = simpson_3_8(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = gaussian_quadrature(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = integrate.quad(f, *lim)[0]
print(calc, "error:", abs(resp-calc))

print("case 4")
f = lambda x: sin(x)**2 - 1
lim = [0, pi]
resp = -pi/2
calc = simpson_1_3(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = simpson_3_8(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = gaussian_quadrature(f, *lim)
print(calc, "error:", abs(resp-calc))
calc = integrate.quad(f, *lim)[0]
print(calc, "error:", abs(resp-calc))
