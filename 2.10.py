import numpy as np
import matplotlib.pyplot as plt


def get_volume(h):
    r = 17.4 / 2
    return np.pi * r ** 2 * h


def polynomial(p, x):
    value = 0
    degree = len(p) - 1
    for i in range(len(p)):
        value = value + p[i] * x ** (degree - i)
    return value


t = [0, 0.92, 1.84, 2.95, 3.87, 4.98, 5.90, 7.01, 7.92,
     8.97, 9.98, 10.92, 10.95, 12.03, 12.95, 13.88,
     14.98, 15.9, 16.83, 17.93, 19.04, 19.96,
     20.84, 22.01, 22.96, 23.88, 24.99, 25.91]

h = [9.68, 9.48, 9.31, 9.13, 8.98, 8.81, 8.69,
     8.52, 8.39, 8.22, 0, 0, 10.82, 10.5, 10.21,
     9.94, 9.65, 9.41, 9.18, 8.92, 8.66, 8.43,
     8.22, 0, 0, 10.59, 10.35, 10.18]

diff_h_0 = np.zeros([len(h), 1])
for i in range(1, len(h)):
    diff_h_0[i - 1] = (h[i] - h[i - 1]) / (t[i] - t[i - 1])

diff_h_0[9:12] = 0
diff_h_0[22:25] = 0

print(diff_h_0)
plt.plot(range(0, len(diff_h_0)), diff_h_0)
plt.show()

y1 = diff_h_0[:9]
y2 = diff_h_0[12:22]
y3 = diff_h_0[25:27]

p0 = np.polyfit(t[:9], y1, 3)
p1 = np.polyfit(t[12:22], y2, 3)
p2 = np.polyfit(t[25:27], y3, 3)

n = 100
x_0 = np.linspace(0, 8.97, n)
y_fit_0 = np.zeros([n, ])
for i in range(n):
    y_fit_0[i] = polynomial(p0, x_0[i])

x_1 = np.linspace(10.95, 20.84, n)
y_fit_1 = np.zeros([n, ])
for i in range(n):
    y_fit_1[i] = polynomial(p1, x_1[i])

x_2 = np.linspace(23.88, 24, 10)
y_fit_2 = np.zeros([10, ])
for i in range(10):
    y_fit_2[i] = polynomial(p2, x_2[i])

int_y0 = np.trapz(y_fit_0, x_0)
int_y1 = np.trapz(y_fit_1, x_1)
int_y2 = np.trapz(y_fit_2, x_2)

print(f'积分后得到{int_y0 + int_y1 + int_y2}')
print(f'日用水量为{get_volume(int_y0 + int_y1 + int_y2)}')