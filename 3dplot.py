# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

"""
faye
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = 12.8, 9.6

ax = plt.axes(projection='3d')

def LoG(x, y, sigma):
    temp = (x ** 2 + y ** 2) / (2 * sigma ** 2)
    return -1 / (np.pi * sigma ** 4) * (1 - temp) * np.exp(-temp)

N = 49
half_N = N // 2
X2, Y2 = np.meshgrid(range(N), range(N))
Z2 = -LoG(X2 - half_N, Y2 - half_N, sigma=8)
X1 = np.reshape(X2, -1)
Y1 = np.reshape(Y2, -1)
Z1 = np.reshape(Z2, -1)

ax = plt.axes(projection='3d')
ax.plot_surface(X2, Y2, Z2, cmap='jet')
