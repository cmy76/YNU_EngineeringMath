import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interp
import scipy.optimize as opt


def iteration(x_pre):
    x_next = (2 - np.exp(x_pre))/10
    return x_next


x = np.ones([20, 1])
xx = np.linspace(1, 20, 20)
for i in range(1, 20):
    x[i] = iteration(x[i - 1])
    if np.abs(x[i] - x[i - 1]) < 10**(-4):
        break
x = x[0:i]
plt.plot(range(0, i), x)
for i in range(i):
    plt.text(xx[i]-1, x[i], str(x[i]))
plt.xticks(range(0, i))
plt.ylabel('n_iter')
plt.ylabel('value')
plt.grid()
plt.show()
print('迭代结果')
print(x)