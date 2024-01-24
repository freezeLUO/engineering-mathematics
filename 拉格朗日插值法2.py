import numpy as np
import matplotlib.pyplot as plt

def lagrange_coefficient(i, x, y):
    s = y[i]
    for j in range(len(x)):
        if j == i:
            continue
        fac = x[i] - x[j]
        s = s / fac
    return s

def lagrange_basis(x1, i, x):
    s = 1
    for j in range(len(x)):
        if j == i:
            continue
        fac = x1 - x[j]
        s = s * fac
    return s

def interpolate(x1, x, y):
    result = 0
    for i in range(len(x)):
        result += lagrange_coefficient(i, x, y) * lagrange_basis(x1, i, x)
    return result

x = [0.0, 0.2, 0.4, 0.6, 0.8]
y = [1.0000, 1.2214, 1.4918, 1.8221, 2.2255]

x1 = 0.13
result = interpolate(x1, x, y)
print("result =", result)
