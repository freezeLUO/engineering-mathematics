import matplotlib.pyplot as plt
import numpy as np

def get_input_coordinates(prompt):
    coordinates = input(prompt).split()
    return [float(num) for num in coordinates]

def calculate_sum(a, x):
    return sum(num**a for num in x)

def fit_polynomial(x, y, power):
    tagx = len(x)
    tagy = len(y)
    if tagx != tagy:
        print("请正确输入坐标!")
        sys.exit()

    matrix1 = np.zeros((power+1, power+1))
    for i in range(power+1):
        for j in range(power+1):
            matrix1[i, j] = calculate_sum(i+j, x)
    matrix1[0, 0] = tagx

    matrix2 = np.zeros((power+1, 1))
    for i in range(power+1):
        matrix2[i, 0] = calculate_sum(i, x) * calculate_sum(i, y)

    inverse_matrix = np.linalg.inv(matrix1)
    product_matrix = np.dot(inverse_matrix, matrix2)

    return list(product_matrix[:, 0])

def main():
    x = get_input_coordinates("请输入x坐标（以空格分隔,回车键结束）：")
    y = get_input_coordinates("请输入y坐标（以空格分隔,回车键结束）：")

    power = int(input("请输入拟合曲线的阶数："))

    coefficients = fit_polynomial(x, y, power)

    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')

    polynomial = np.poly1d(coefficients)

    x_values = np.linspace(min(x), max(x), 100)
    y_values = polynomial(x_values)

    plt.plot(x_values, y_values)
    plt.show()

if __name__ == "__main__":
    main()