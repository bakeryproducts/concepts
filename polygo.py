# Polygon from matplotlib and Area

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def PolyArea(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def DropPoleB(x, y, *, heiB=1, lenB=2):
    poleB = np.array([[0, 0], [0, heiB], [lenB, heiB], [lenB, 0]], dtype=float)
    poleB[:, 0] += x
    poleB[:, 1] += y
    return poleB


pat = []
n = 100
intervalX, intervalY = 20, 15
lenA, heiA = 8, 4


x0A, y0A = intervalX / 2 - lenA / 2, intervalY / 2 - heiA / 2
targetA = np.array([[0, 0], [0, heiA], [lenA, heiA], [lenA, 0]], dtype=float)
targetA[:, 0] += x0A
targetA[:, 1] += y0A
polygonA = Polygon(targetA, True)
pat.append(polygonA)

for i in range(n):
    xpoleB, ypoleB = intervalX * np.random.rand(), intervalY * np.random.rand()
    polygonB = Polygon(DropPoleB(xpoleB, ypoleB), True)
    pat.append(polygonB)


p = PatchCollection(pat, alpha=.8)
colors = 250 * np.random.rand(len(pat))
p.set_array(np.array(colors))

fig, ax = plt.subplots()
ax.add_collection(p)

for poly in pat:
    pp = np.array(poly.get_xy())
    print(PolyArea(pp[:, 0], pp[:, 1]))


ax.set_xlim([0, intervalX])
ax.set_ylim([0, intervalY])
plt.show()
