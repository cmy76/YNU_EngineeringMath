import numpy as np
import matplotlib.pyplot as plt


def function1(n_iter=100): #方法1
    y = np.zeros([n_iter, 1])
    y[0] = np.log(6) - np.log(5)
    for i in range(1, n_iter):
        y[i] = 1 / i - 5 * y[i - 1]
    return y


def function2(n_iter=99): #方法2
    y = np.zeros([n_iter, 1])
    y[n_iter-1] = 0.1815 * 10 ** (-2)
    for i in range(2, n_iter):
        y[n_iter - i] = 1 / (5 * i) - (1 / 5) * y[n_iter - i + 1]
    return y


n = 100
x = np.linspace(0, n, n)
#迭代
y1 = function1(n)
y2 = function2(n)

#绘图
plt.subplot(2, 1, 1)
plt.plot(x[0:98], y2[0:98])
plt.title('Algorithm 2')
plt.ylabel('value')
plt.subplot(2, 1, 2)
plt.plot(x[0:98], y1[0:98])
plt.xlabel('n_iter')
plt.ylabel('value')
plt.title('Algorithm 1')
plt.show()