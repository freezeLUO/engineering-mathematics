import numpy as np
def find_section(func, x0, h=1):
 
    x1 = x0 + h
    if func(x1) > func(x0):
        h = -h
        x1 = x0 + h
    
    while func(x1) < func(x0):
        x1 = x1 + h
        h *= 2
    if x0 < x1:
        return (x0, x1)
    else:
        return (x1, x0)

def golden_section_search(func,x0,tol=0.2):
    phi = (5**0.5 - 1)/2
    
    a, b = find_section(func,x0)
    c = a + phi * (b - a)
    d = a + (1 - phi) * (b - a)
    t = 0

    while abs(b - a) > tol:
        t += 1
        if func(c) < func(d):
            a = d
            d = c
            c = a + phi * (b - a)
        else:
            b = c
            c = d
            d = a + (1 - phi) * (b - a)

    return ((a + b) / 2, t)


def f1(x):
    return 3*(x**3)-4*x+2

x_min1,t = golden_section_search(f1,0)
a, b = find_section(f1,0)
print(f"搜索区间为({a},{b})")
print("x_min1 =",x_min1)
print("黄金分割法迭代次数为:",t)

