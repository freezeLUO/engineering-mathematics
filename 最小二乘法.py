import matplotlib.pyplot as plt
import numpy as np
import sys

x = []
y = []
tagx = 0
tagy = 0
#设置想要拟合曲线的阶数
power = int(input("请输入拟合曲线的阶数："))

#输入x坐标
linex = input("请输入x坐标（以空格分隔,回车键结束）：")
for num in linex.split():
    x.append(float(num))
    tagx += 1

#输入y坐标
liney = input("请输入y坐标（以空格分隔,回车键结束）：")
for num in liney.split():
    y.append(float(num))
    tagy += 1
    
if(tagx != tagy):
    print("请正确输入坐标!")
    sys.exit()

def sumx(a): #计算a次方的和
    tag_elements = [num**a for num in x]
    return sum(tag_elements)
        
def sumy(a):#计算y
    tag_elements = [num**a for num in x]
    a = np.array(tag_elements)
    b = np.array(y)
    c = np.multiply(a, b)
    return sum(c)
#生成一个0矩阵
matrix1 = np.zeros((power+1, power+1))

#填入矩阵
for i in range(0, power+1):
    for j in range(0, power+1):
        matrix1[i,j] = sumx(i+j)
matrix1[0,0] = tagx


matrix2 = np.zeros((power+1, 1))
for i in range(0, power+1):
    matrix2[i,0] = sumy(i)


inverse_matrix = np.linalg.inv(matrix1)
product_matrix = np.dot(inverse_matrix, matrix2)
print(product_matrix)
arrf = []
for i in range(0, power+1):
    arrf.append(product_matrix[i,0])
reversed_arr = arrf[::-1]

plt.scatter(x, y)

plt.xlabel('X')
plt.ylabel('Y')
polynomial = np.poly1d(reversed_arr)


x_values = np.linspace(int(min(x)), int(max(x)), int(max(y)))
# 计算多项式在x值范围内的y值
y_values = polynomial(x_values)

# 使用pyplot的plot函数绘制多项式
plt.plot(x_values, y_values)
plt.show()