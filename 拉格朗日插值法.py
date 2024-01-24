import numpy as np
import matplotlib.pyplot as plt
x = [0.0, 0.2, 0.4, 0.6, 0.8] #x
y = [1.0000, 1.2214, 1.4918, 1.8221, 2.2255] #e^x
power = len(x) #阶数

def Lagrange1(i,x,y):#i为第i项,返回每一项的整数系数
    s = y[i]
    for j in range(power):
        if j==i:
            continue
        fac = x[i]-x[j]
        s = s/fac
    return s

def Lagrange2(x1,i,x,y): #x1为待定系数,i为第i项
    s = 1
    for j in range(power):
        if j==i:
            continue
        fac = x1-x[j]
        s = s*fac
    return s
        
def my_function(x1,power):
    fin = 0
    for i in range(power):
        fin = fin + Lagrange1(i,x,y)*Lagrange2(x1,i,x,y)
    return fin
print("result = ",my_function(0.13,power))
    