# Polygon from matplotlib and Area

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def PolyArea(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


pat = []
n = 5
p1=np.array([[2,0],[0,0],[0,1],[4,1],
            [4,2],[2,2],[2,1]
            ])

for i in range(1):
    #polygon = Polygon(np.random.rand(n, 2), True)
    polygon = Polygon(p1)
    pat.append(polygon)

p = PatchCollection(pat, alpha=.8)
colors = 100 * np.random.rand(len(pat))
p.set_array(np.array(colors))

fig, ax = plt.subplots()
ax.add_collection(p)

for poly in pat:
    pp = np.array(poly.get_xy())

    print(PolyArea(pp[:, 0], pp[:, 1]))
ax.set_xlim([0,5])
ax.set_ylim([0,5])
plt.show()
