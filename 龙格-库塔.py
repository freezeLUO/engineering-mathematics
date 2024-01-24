#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import math
import matplotlib.pyplot as plt


# In[11]:


def func(x,y):
    return -y

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

def euler3(x0,y0,h,N): 
    n=1
    x_values = [x0]
    y_values = [y0]
    while(n<N):
        x1=x0+h
        y_p=y0+h*func(x0,y0) 
        y1=y0+h*func(x1,y_p)
        y1=(y_p + y1)/2
        x0=x1
        y0=y1
        n+=1
        x_values.append(x1)
        y_values.append(y1)
    return x_values,y_values


# In[12]:


x0=0
y0=1
h=0.1
N=60
x_1,y_1=rungekutta(x0,y0,h,N)
x_3,y_3=euler3(x0,y0,h,N)


# In[13]:


x_c = np.arange(0, 6, 0.1)
y_c = np.exp(-x_c)

plt.plot(x_1, y_1, color='red',label='R-K')
plt.plot(x_3, y_3, color='green',label='Euler')
plt.plot(x_c, y_c, color='blue',label='y = e^(-x)')



plt.xlabel('x_c')
plt.ylabel('y_c')
plt.title('Plot of y = e^(-x)')
plt.grid(True)
plt.legend()
plt.show()


# In[ ]:




