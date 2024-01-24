# Doolittle (杜利特尔) 直接分解法
import numpy as np

def Doolittle(A, b):
    n = len(b)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    #第一步
    for i in range(n):
        U[0, i] = A[0, i]
        L[i, 0] = A[i, 0] / U[0, 0]
    #第二步
    for i in range(1, n):
        for j in range(i, n):
             U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
             L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]
    return L,U



# Ax = b
A = np.array([[6, 7, 5],
              [7, 13, 8],
              [5, 8, 6]])
b = np.array([9, 10, 9])

a1,b1 = Doolittle(A, b)
print("L=\n",a1)
print("U=\n",b1)