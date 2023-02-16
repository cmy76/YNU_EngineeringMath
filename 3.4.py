import numpy as np
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

path = 'Final/Data\\附件3-区域高程数据.xlsx'

xx = np.linspace(0, 2913 * 38.2, 2913)
yy = np.linspace(0, 2775 * 38.2, 2774)
X, Y = np.meshgrid(xx, yy)
df = pd.read_excel(path)

Z = np.array(df)

fig = plt.figure()  # 定义新的三维坐标轴
ax3 = plt.axes(projection='3d')

ax3.plot_surface(X, Y, Z)
plt.show()
