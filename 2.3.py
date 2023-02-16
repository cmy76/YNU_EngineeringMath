import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interp
import scipy.optimize as opt


def mse(y, y_fit):
    y = y.reshape([len(y), 1])
    t = (np.power(y - y_fit, 2))
    mse = 1 / len(y) * sum(t)
    return mse


def func1(x, a, b):
    return a + b * np.sin(np.pi * x / 10)


def getPolyFitValue(p, x):
    degree = len(p)
    value = 0
    for i in range(degree):
        value = value + p[i] * np.power(x, degree - 1 - i)
    return value


def plot(p, popt, x, y):
    poly = np.zeros([len(x), 1])
    nonpoly = np.zeros([len(x), 1])
    for i in range(len(x)):
        poly[i] = getPolyFitValue(p, x[i])
        nonpoly[i] = func1(x[i], popt[0], popt[1])
    mse_poly = mse(y, poly)
    mse_nonpoly = mse(y, nonpoly)
    print(f"多项式拟合的MSE为{mse_poly}")
    print(f"非多项式拟合的MSE为{mse_nonpoly}")
    plt.subplot(2, 1, 1)
    plt.plot(x, poly, 'ro-')
    plt.ylabel('fit')
    plt.title('poly')
    plt.subplot(2, 1, 2)
    plt.plot(x, nonpoly, 'bo-')
    plt.xlabel('x')
    plt.ylabel('fit')
    plt.title('non_poly')
    plt.show()


y0 = [5.4167, 5.5196, 5.7428, 5.8796, 6.1465, 6.2828, 6.4653, 6.5994, 6.7209, 6.6207]
y1 = [6.5859, 6.7297, 6.9172, 7.2538, 7.4542, 7.7368, 7.8534, 8.2992, 8.7177, 9.0859]
y2 = [9.2420, 9.3717, 9.4974, 9.7542, 9.8705, 10.1541, 10.2495, 10.3475]

y0 = np.concatenate([y0, y1])
y = np.concatenate([y0, y2])

x0 = np.linspace(1, 23, 23)
x1 = [25, 26, 28, 30, 31]
x = np.concatenate([x0, x1])

p = np.polyfit(x, y, 3)

print(f'线性拟合函数的系数为{p}')
print(f'线性拟合函数在27和32的值分别为{getPolyFitValue(p, 27)}和{getPolyFitValue(p, 32)}')

popt, pcov = opt.curve_fit(func1, x, y)

print(f'非线性拟合函数的系数为{popt}')
print(f'非线性拟合函数在27和32的值分别为{func1(27, popt[0], popt[1])}和{func1(32, popt[0], popt[1])}')

plot(p, popt, x, y)
