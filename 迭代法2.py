import math


def equation(x):
    return math.log(x + 2)


def equation1(x):
    return math.exp(x) - 2


def newton(func, guess, max_step, tol):
    f1 = func(guess)
    f2 = func(f1)
    step_count = 0  # 将step_count设为局部变量
    while (abs(f1 - f2) > tol) and (step_count < max_step):
        f1 = func(f1)
        f2 = func(f2)
        step_count += 1
    return f2, step_count  # 返回结果和迭代步数


result1, steps1 = newton(equation, 2, 100, 1e-6)
result2, steps2 = newton(equation1, 0, 100, 1e-6)

print("求得的解1为:", result1)
print("迭代步数为:", steps1)
print("求得的解2为:", result2)
print("迭代步数为:", steps2)