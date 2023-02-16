import numpy as np
import sympy as sp


def jacobian(f, x):  # 雅可比矩阵，求一阶导数
    a, b = np.shape(x)  # 判断变量维度
    x1, x2 = sp.symbols('x1 x2')  # 定义变量，如果多元的定义多元的
    x3 = [x1, x2]  # 将1变量放入列表中，方便查找和循环。有几个变量放几个
    df = np.array([[0.00000], [0.00000]])  # 定义一个空矩阵，将雅可比矩阵的值放入，保留多少位小数，小数点后面就有几个0。n元变量就加n个[]
    for i in range(a):  # 循环求值

        df[i, 0] = sp.diff(f, x3[i]).subs({x1: x[0][0], x2: x[1][0]})  # 求导和求值,n元的在subs后面补充

    return df


def hesse(f, x):  # hesse矩阵
    a, b = np.shape(x)
    x1, x2 = sp.symbols('x1 x2')
    x3 = [x1, x2]
    G = np.zeros((a, a))
    for i in range(a):
        for j in range(a):
            G[i, j] = sp.diff(f, x3[i], x3[j]).subs({x1: x[0][0], x2: x[1][0]})  # n元的在subs后面补充

    return G


def dfp_newton(f, x, iters):
    """
    实现DFP拟牛顿算法
    :param f: 原函数
    :param x: 初始值
    :param iters: 遍历的最大迭代次数
    :return: 最终更新完毕的x值
    """
    a = 1  # 定义初始步长

    H = np.eye(2)  # 初始化正定矩阵
    G = hesse(f, x)  # 初始化Hesse矩阵

    epsilon = 1e-3  # 一阶导g的第二范式的最小值（阈值）
    for i in range(1, iters):
        g = jacobian(f, x)

        if np.linalg.norm(g) < epsilon:
            xbest = []
            for a in x:
                xbest.append(round(a[0]))  # 将结果从矩阵中输出放到列表中并四舍五入
            break
        # 下面的迭代公式
        d = -np.dot(H, g)

        a = -(np.dot(g.T, d) / np.dot(d.T, np.dot(G, d)))

        # 更新x值
        x_new = x + a * d
        print("第 %d 次结果" % i)
        print(x_new)
        g_new = jacobian(f, x_new)
        y = g_new - g

        s = x_new - x
        # 更新H
        H = H + np.dot(s, s.T) / np.dot(s.T, y) - np.dot(H, np.dot(y, np.dot(y.T, H))) / np.dot(y.T, np.dot(H, y))
        # 更新G
        G = hesse(f, x_new)
        print(x)
        x = x_new

    return xbest


x1, x2 = sp.symbols('x1 x2')  # 例子
x = np.array([[0], [0]])
f = 3/2*x1**2 + 1/2*x2**2 - x1*x2 - 2*x1
print(dfp_newton(f, x, 20))