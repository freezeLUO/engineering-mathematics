import numpy as np
import matplotlib.pyplot as plt
import math

x = [0.0, 0.2, 0.4, 0.6, 0.8] #x
y = [1.0000, 1.2214, 1.4918, 1.8221, 2.2255] #e^x

max_order = len(x) - 1 #最大阶数
h = x[1] - x[0] #步长

#向前差分
delta_y = []


for i in range(len(x)-1):
    delta_y.append(y[i+1] - y[i])
print(delta_y)

zero_matrix = np.zeros((max_order, max_order))
zero_matrix[0, ] = delta_y
print(zero_matrix)

for i in range(max_order):
    if i==0:
        continue
    for j in range(max_order-i):
        zero_matrix[i, j] = zero_matrix[i-1, j+1] - zero_matrix[i-1, j]
print(zero_matrix)
delta_y1 = []
delta_y1 = zero_matrix[:,0]
print(delta_y1)

def newt(h,x1,delta_y1,i): #每一项的值
    s = 1
    for j in range(i):
        fac = x1-x[j]
        s = s*fac
    s = s*delta_y1[i-1]/(math.factorial(i)*(h**i))
    return s
    
fin = 0
for i0 in range(1, max_order):
    fin += newt(h,0.13,delta_y1,i0)
fin += y[0]

print(fin)
    