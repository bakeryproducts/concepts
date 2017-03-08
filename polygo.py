# Polygon from matplotlib and Area
import numpy as np
import matplotlib.pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import Polygon

def PolyArea(poly):
    x,y = poly.exterior.xy
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def DropPoleB(x0, y0, *, heiB=1, lenB=2):
    poleB = np.array([[0, 0], [0, heiB], [lenB, heiB], [lenB, 0]], dtype=float)
    poleB[:, 0] += x0
    poleB[:, 1] += y0
    return poleB


def drawpoly(poly, splot, clr=None, al=.5):
    if clr is None:
        clr = np.random.rand(3, 1)
    polypatch = PolygonPatch(poly, color=clr, alpha=al)
    splot.add_patch(polypatch)


fig, ax = plt.subplots()
polygons = []

n = 120
intervalX, intervalY = 20, 15
lenA, heiA = 8, 4

x0A, y0A = intervalX / 2 - lenA / 2, intervalY / 2 - heiA / 2
targetA = np.array([[0, 0], [0, heiA], [lenA, heiA], [lenA, 0]], dtype=float)
targetA[:, 0] += x0A
targetA[:, 1] += y0A
polygonA = Polygon(targetA)
print(PolyArea(polygonA))
drawpoly(polygonA, ax, clr='g', al=1)

for i in range(n):
    xpoleB, ypoleB = intervalX * np.random.rand(), intervalY * np.random.rand()
    polygonB = Polygon(DropPoleB(xpoleB, ypoleB))
    polygons.append(polygonB)
    drawpoly(polygonB, ax, al=.2)

hits = [polygonA.intersection(poly) for poly in polygons]
damagemap = [hit for hit in hits if hit.geom_type == 'Polygon']

unionarea = damagemap[0]
for area in damagemap:
    unionarea = area.union(unionarea)

drawpoly(unionarea, ax, clr='r', al=.9)

totalarea=0
for area in unionarea:
    totalarea+=PolyArea(area)

print(totalarea)

ax.set_xlim([0, intervalX])
ax.set_ylim([0, intervalY])
plt.show()
