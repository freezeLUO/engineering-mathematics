import numpy as np
def jacobi(A, b, step=100, f=1e-6):
    n = len(b)
    x = np.zeros(n)
    ii = 0
    for i1 in range(step):
        ii = ii + 1
        new_x = np.zeros(n)
        for i in range(n):
            new_x[i] = b[i]
            for j in range(n):
                if j < i:
                    new_x[i] -= A[i, j] * new_x[j]
                elif (j > i):
                    new_x[i] -= A[i, j] * x[j]
            
            new_x[i] /= A[i, i]

        if np.linalg.norm(new_x - x) < f:
            break
        x = new_x

    return x,ii
        
   
A = np.array([[10, -1, 2, 0],
              [-1, 11, -1, 3],
              [2, -1 ,10, -1],
             [0, 3, -1, 8]])

b = np.array([6, 25, -11, 15])
x,y = jacobi(A, b)
print(x)
print("迭代了",y)
