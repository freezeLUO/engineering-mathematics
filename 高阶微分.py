import numpy as np
import math
import matplotlib.pyplot as plt

def func(x,y):
    return y+x
def func1(x,y):
    return x


def euler1(x0,y0,h,N): #向前
    n=1
    x_values = [x0]
    y_values = [y0]
    while(n<N):
        x1=x0+h
        y1=y0+h*func(x0,y0) 
        n+=1
        x0=x1
        y0=y1
        x_values.append(x1)
        y_values.append(y1)
    return x_values,y_values

def rungekutta(x0,y0,h,N):
    n = 1
    x_values = [x0]
    y_values = [y0]
    while n<N:
        x1=x0+h
        k1=func(x0,y0)
        k2=func(x0+h/2,y0+h*k1/2)
        k3=func(x0+h/2,y0+h*k2/2)
        k4=func(x1,y0+h*k3)
        y1=y0+h*(k1+2*k2+2*k3+k4)/6
        x0=x1
        y0=y1
        n+=1
        x_values.append(x1)
        y_values.append(y1)
    return x_values,y_values

def Fina(x,y,h,N):
    x_values = [x[0]]
    y_values = [y[0]*h]
    x0 = x[0]
    y0 = y[0]*h
    n = 1
    while(n<N):
        x1=x0+h;
        y1=y_values[n-1] + h*y[n]
        n = n+1
        x0=x1
        y0=y1
        x_values.append(x1)
        y_values.append(y1)
    return x_values,y_values

x0=0
y0=1

h=0.1
N=60
x_2,y_2=rungekutta(x0,y0,h,N)
x_3,y_3=Fina(x_2,y_2,h,N)

x_c = np.arange(0, 6, 0.1)
plt.plot(x_3, y_3, color='green',label='y')
y_c = -2+2*np.exp(x_c)-0.5*x_c**2-x_c
plt.plot(x_c, y_c,label='ori')

plt.xlabel('x_c')
plt.ylabel('y_c')

plt.grid(True)
plt.legend()
plt.show()
