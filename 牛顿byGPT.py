import numpy as np
import math

def forward_difference(y):
    return [y[i+1] - y[i] for i in range(len(y)-1)]

def divided_difference_table(y):
    max_order = len(y) - 1
    delta_y = forward_difference(y)
    
    table = np.zeros((max_order, max_order))
    table[0, :] = delta_y
    
    for i in range(1, max_order):
        for j in range(max_order - i):
            table[i, j] = table[i-1, j+1] - table[i-1, j]
    
    return table

def newton_interpolation(x, y, x1):
    max_order = len(x) - 1
    h = x[1] - x[0]
    delta_y1 = divided_difference_table(y)[:, 0]
    
    result = y[0]
    for i in range(1, max_order):
        term = delta_y1[i-1] / (math.factorial(i) * (h**i))
        for j in range(i):
            term *= (x1 - x[j])
        result += term
    
    return result

x = [0.0, 0.2, 0.4, 0.6, 0.8]
y = [1.0000, 1.2214, 1.4918, 1.8221, 2.2255]
x1 = 0.13

result = newton_interpolation(x, y, x1)
print("result =", result)
