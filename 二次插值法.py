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
    
def quadratic_interpolation(func,x0,tol=0.2,max_iter=100):
    x0,x2 = find_section(func, x0)
    x1 = (x0+x2)/2

    for i in range(max_iter):
        f0, f1, f2 = func(x0), func(x1), func(x2)
        xp = 0.5*((x1**2-x2**2)*f0 + (x2**2-x0**2)*f1 + (x0**2-x1**2)*f2)
        xp = xp/((x1-x2)*f0 + (x2-x0)*f1 + (x0-x1)*f2)
        fp = func(xp)
        if abs(xp - x1) < tol:
            return xp
        # 更新点
        if xp > x1:
            x0, x1, x2 = x1, xp, x2
        else:
            x0, x1, x2 = x0, xp, x1    
    return xp

def f1(x):
    return 3*(x**3)-4*x+2

x_min2 = quadratic_interpolation(f1,0)
a, b = find_section(f1,0)
print(f"搜索区间为({a},{b})")
print("x_min2 =",x_min2)