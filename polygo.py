import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

pat = []
n=3

for i in range(n):
    polygon = Polygon(np.random.rand(n,2),True)
    pat.append(polygon)

p = PatchCollection(pat,alpha=.4)
colors = 100*np.random.rand(len(pat))
p.set_array(np.array(colors))

fig,ax = plt.subplots()
ax.add_collection(p)
pp=np.array(pat[0].get_xy())
print(pp[0])

plt.show()