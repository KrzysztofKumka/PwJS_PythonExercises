import numpy as np
print("Enter the coefficients a, b and c")

a, b, c = map(float, input().split())

delta = b*b - 4*a*c

if delta > 0:
    x1 = (-b + np.sqrt(delta)/2*a)
    x2 = (-b - np.sqrt(delta)/2*a)
    print("Roots of the quadratic equation x1 = " + np.str("%.2f" % x1) + " x2 = " + np.str("%.2f" % x2))

if delta == 0:
    x0 = -b/2*a
    print("Root of the quadratic equation: x0 = " + x0)

if delta < 0:
    print("Equation without roots in the domain of real numbers.")
