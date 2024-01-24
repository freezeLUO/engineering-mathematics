import math


def equation(x):
    return math.log(x + 2)


def equation1(x):
    return math.exp(x) - 2


def newton(func, guess, max_step, tol):
    f1 = func(guess)
    f2 = func(f1)
    global step_count
    step_count = 0
    while (abs(f1 - f2) > tol) and (step_count < max_step):
        f1 = func(f1)
        f2 = func(f2)
        step_count += 1
    return f2


print("求得的解1为:", newton(equation, 2, 100, 1e-6))
print("迭代步数为:", step_count)
print("求得的解2为:", newton(equation1, 0, 100, 1e-6))
print("迭代步数为:", step_count)
