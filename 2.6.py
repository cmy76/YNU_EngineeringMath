# !/usr/bin/python
# -*- coding:utf-8 -*-
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

from scipy.optimize import minimize
import numpy as np


def fun():
    v = lambda x: 3/2*x[0]**2 + 1/2*x[1]**2 - x[0]*x[1] - 2*x[0]
    return v


x0 = np.asarray((0, 0))  # 初始猜测值
res = minimize(fun(), x0, method='SLSQP')
print(res)
print(res.success)


def sinvar(fun):
    s_p = solve(diff(fun))  # stationary point
    return s_p


def value_enter(fun, x, i):
    value = fun[i].subs(x1, x[0]).subs(x2, x[1])
    return value


def grandient_l2(grand, x_now):
    grand_l2 = sqrt(pow(value_enter(grand, x_now, 0), 2) + pow(value_enter(grand, x_now, 1), 2))
    return grand_l2


def msd(x_init, obj):
    i = 1
    grandient_obj = np.array([diff(obj, x1), diff(obj, x2)])
    error = grandient_l2(grandient_obj, x_init)
    plt.plot(x_init[0], x_init[1], 'ro')
    while (error > 0.001):
        if i == 1:
            grandient_obj_x = np.array([value_enter(grandient_obj, x_init, 0), value_enter(grandient_obj, x_init, 1)])
            t = symbols('t')
            x_eta = x_init - t * grandient_obj_x
            eta = sinvar(obj.subs(x1, x_eta[0]).subs(x2, x_eta[1]))
            x_new = x_init - eta * grandient_obj_x
            print(x_new)
            i = i + 1
            error = grandient_l2(grandient_obj, x_new)
            plt.plot(x_new[0], x_new[1], 'ro')
        else:
            grandient_obj_x = np.array([value_enter(grandient_obj, x_new, 0), value_enter(grandient_obj, x_new, 1)])
            t = symbols('t')
            x_eta = x_new - t * grandient_obj_x
            eta = sinvar(obj.subs(x1, x_eta[0]).subs(x2, x_eta[1]))
            x_new = x_new - eta * grandient_obj_x
            print(x_new)
            i = i + 1
            error = grandient_l2(grandient_obj, x_new)
            plt.plot(x_new[0], x_new[1], 'ro')
    plt.show()


x_0 = np.array([0, 0], dtype=float)
x1 = symbols("x1")
x2 = symbols("x2")
result = msd(x_0, 3/2*x1**2 + 1/2*x2**2 - x1*x2 - 2*x1)
