import sys

def equation(x):
    # 定义要解的方程
    return x**6 - x - 1

def dichotomy(func, a, b, tol, max_step):
    if ((func(a) * func(b)) >= 0):
        print("错误：初始区间 [a, b] 必须包含一个根")
        sys.exit(1)  # 终止程序

    global step_count
    step_count = 0

    while (((b - a) / 2 > tol/2) and (step_count < max_step)):
        c = (a+b)/2
        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        step_count += 1
        
    return (a+b)/2

a = 1
b = 2
tol = 1e-3
max_step = 1000

result = dichotomy(equation, a, b, tol, max_step)

print("找到的根为：", result)
print("对应的值为：", equation(result))
print("迭代的次数为：", step_count)