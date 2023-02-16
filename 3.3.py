import cv2
import numpy as np
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import cvxpy as cp

path = 'Final/Data\\附件2-目标点数据.xlsx'


def distance(p0, p1):
    return np.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


def getPosDict(path):
    df = pd.read_excel(path)
    d_pos = dict()
    for row in df.index:
        pointName = df.at[row, '顶点']
        x = df.at[row, 'x坐标']
        y = df.at[row, 'y坐标']
        d_pos[pointName] = [x, y]
    return d_pos


def read_data(path, d_pos):
    G = nx.Graph()
    pos = dict()
    df = pd.read_excel(path)
    print(df)
    node_shape = []
    for row in df.index:
        pointName = df.at[row, '顶点']
        x = df.at[row, 'x坐标']
        y = df.at[row, 'y坐标']
        pos[pointName] = (x, y)

        cls = df.at[row, '顶点类别']
        if cls == 1:
            G.add_node(pointName)
            node_shape.append('*')
        elif cls == 2:
            G.add_node(pointName, node_shape='s')
            node_shape.append('X')
        else:
            G.add_node(pointName, node_shape='s')
            node_shape.append('.')
        plt.scatter(x, y, marker=node_shape[-1])
        plt.text(x, y, pointName, fontsize=8)
        # plt.text(x, y, str(x)+','+str(y), fontsize=4)
        near_p0 = df.at[row, '相邻的顶点1']
        near_p0 = str(near_p0)
        if near_p0 != 'nan':
            d = distance(d_pos[near_p0], [x, y])
            G.add_edge(near_p0, pointName, weight=d)
        near_p1 = df.at[row, '相邻的顶点2']
        near_p1 = str(near_p1)
        if near_p1 != 'nan':
            d = distance(d_pos[near_p1], [x, y])
            G.add_edge(near_p1, pointName, weight=d)
        near_p2 = df.at[row, '相邻的顶点3']
        near_p2 = str(near_p2)
        if near_p2 != 'nan':
            d = distance(d_pos[near_p2], [x, y])
            G.add_edge(near_p2, pointName, weight=d)
    return G, pos, row, node_shape

d_pos = getPosDict(path)
G, pos, row, node_shape = read_data(path, d_pos)
T = nx.minimum_spanning_tree(G)
print(f'最小生成树{T.nodes}')
nx.draw(G, pos, width=0.1, alpha=1, node_shape='*', font_size=1, node_size=10)
plt.savefig("graph")
# plt.show()
print(len(G))

minWPath1 = nx.dijkstra_path(G, source='L', target='R3')  # 顶点 0 到 顶点 17 的最短加权路径
# 两个指定顶点之间的最短加权路径的长度
lMinWPath1 = nx.dijkstra_path_length(G, source='L', target='R3')  #最短加权路径长度
print("\n问题1: 无限制条件")
print("L 到 R3 的最短加权路径: ", minWPath1)
for point in minWPath1:
    plt.scatter(d_pos[point][0], d_pos[point][1], marker='o')
print("L 到 R3 的最短加权路径长度: ", lMinWPath1)

minWPath1 = nx.dijkstra_path(G, source='P', target='L2')  # 顶点 0 到 顶点 17 的最短加权路径
# 两个指定顶点之间的最短加权路径的长度
lMinWPath1 = nx.dijkstra_path_length(G, source='P', target='L2')  #最短加权路径长度
for point in minWPath1:
    plt.scatter(d_pos[point][0], d_pos[point][1], marker='v')
plt.savefig("cut")
plt.show()
print("\n问题1: 无限制条件")
print("P 到 L2 的最短加权路径: ", minWPath1)
print("P 到 L2 的最短加权路径长度: ", lMinWPath1)
