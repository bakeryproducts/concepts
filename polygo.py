# Polygon from matplotlib and Area
from shapely.geometry import Polygon as ppgon
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def PolyArea(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def DropPoleB(x0, y0, *, heiB=1, lenB=2):
    poleB = np.array([[0, 0], [0, heiB], [lenB, heiB], [lenB, 0]], dtype=float)
    poleB[:, 0] += x0
    poleB[:, 1] += y0
    return poleB

fig, ax = plt.subplots()

polygons = []
shapgons=[]
n = 150
intervalX, intervalY = 20, 15
lenA, heiA = 8, 4


x0A, y0A = intervalX / 2 - lenA / 2, intervalY / 2 - heiA / 2
targetA = np.array([[0, 0], [0, heiA], [lenA, heiA], [lenA, 0]], dtype=float)
targetA[:, 0] += x0A
targetA[:, 1] += y0A
polygonA = Polygon(targetA, True)
polygons.append(polygonA)
shapA = ppgon(targetA)
print(PolyArea(targetA[:,0],targetA[:,1]))

for i in range(n):
    xpoleB, ypoleB = intervalX * np.random.rand(), intervalY * np.random.rand()
    polygonB = Polygon(DropPoleB(xpoleB, ypoleB), True)
    polygons.append(polygonB)
    shapgons.append(ppgon(DropPoleB(xpoleB, ypoleB)))

p = PatchCollection(polygons, alpha=.5)
colors = 250 * np.random.rand(len(polygons))
p.set_array(np.array(colors))

ax.add_collection(p)

for poly in shapgons:
    #pp = np.array(poly.get_xy())
    #print(PolyArea(pp[:, 0], pp[:, 1]))
    # x,y=poly.exterior.xy
    # ax.plot(x, y, color='#6699cc', alpha=0.9,
    #     linewidth=3, solid_capstyle='round', zorder=2)
    pass
inters=[shapA.intersection(p1) for p1 in shapgons]
bigpoly=[]
for el in inters:
    if el.geom_type == 'Polygon':
        x,y=el.exterior.xy
        #ax.plot(x,y,linewidth=1,color='r')
        bigpoly.append(el)

sum=bigpoly[0]

for el in bigpoly:
    sum=el.union(sum)
totarea=0

for p in sum:
    x,y = p.exterior.xy
    ax.plot(x,y,color='r')
    totarea+=PolyArea(x,y)


print(totarea)

ax.set_xlim([0, intervalX])
ax.set_ylim([0, intervalY])
plt.show()
