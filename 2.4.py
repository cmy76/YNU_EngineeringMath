import numpy as np
from scipy.linalg import lu
from scipy.linalg import inv
A = np.mat([[5, 1, -1, -2], [2, 8, 1, 3], [1, -2, -4, -1], [-1, 3, 2, 7]])
b = np.array([-2, -6, 6, 12])

p, L, U = lu(A)
print(f'L为{L}')
print(f'U为{U}')

x = np.matmul(inv(U), np.matmul(inv(L), b))
print(f'解得方程为{x}')