import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as pyplot

#输入数据
x = [0.40, 0.55, 0.65, 0.80, 0.90, 1.05]
y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]

#线性插值
f_linear = interp.interp1d(x, y, 'linear')

#三次样条
f_cubic = interp.interp1d(x, y, 'cubic')

xx = np.linspace(0.40, 1.05, 20)
yy1 = f_linear(xx)
yy2 = f_cubic(xx)

plt.plot(x, y, 'ro-')
plt.plot(xx, yy1, 'bo-')
plt.plot(xx, yy2, 'yo-')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['original', 'linear', 'cubic'])
plt.show()

#求值
print(f'线性插值函数在0.596的值为{f_linear(0.596)}')
print(f'三次样条插值函数在0.596的值为{f_cubic(0.596)}')