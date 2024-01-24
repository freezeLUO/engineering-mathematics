import numpy as np


def gaussian_elimination(A, b):

    matrix1 = np.column_stack((A, b))

    for i in range(len(b)):
        # 找到最大的行
        max_row_index = np.argmax(abs(matrix1[i:, i])) + i
        # 最大的行与第一行交换
        matrix1[[i, max_row_index]] = matrix1[[max_row_index, i]]

        matrix1[i] = matrix1[i]/matrix1[i, i]  # 第一行的系数化1

        for j in range(len(b)):
            if (j != i):
                m = matrix1[j, i]
                matrix1[j] = matrix1[j] - m * matrix1[i]

    solution = matrix1[:, -1]

    return solution


# Ax = b
A = np.array([[0.729, 0.81, 0.9],
              [1, 1, 1],
             [1.331, 1.21, 1.1]])
b = np.array([0.6867, 0.8338, 1.000])
print("矩阵为：")
print(np.column_stack((A, b)))

result = gaussian_elimination(A, b)
print("\n解为:\n", result)
