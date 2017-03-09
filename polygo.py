# Polygon from matplotlib and Area
import numpy as np
import matplotlib.pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import Polygon
from shapely.ops import cascaded_union
import time


def PolyArea(poly):
    x, y = poly.exterior.xy
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def DropPoleB(N, x0, y0, *, heiB=1., lenB=2.):
    poleB = np.array(N * [[[0, 0], [0, heiB], [lenB, heiB], [lenB, 0]]], dtype=float)
    poleB[:, :, 0] += np.repeat(x0, 4).reshape(n, 4)
    poleB[:, :, 1] += np.repeat(y0, 4).reshape(n, 4)
    return poleB


def drawpoly(poly, splot, clr=None, al=.5):
    if clr is None:
        clr = np.random.rand(3, 1)
    polypatch = PolygonPatch(poly, color=clr, alpha=al)
    splot.add_patch(polypatch)


start = time.perf_counter()
fig, ax = plt.subplots()
n = 400
intervalX, intervalY = 20, 15
lenA, heiA = 8, 4
lenB, heiB = 2, 1
polearea = lenB * heiB

x0A, y0A = intervalX / 2 - lenA / 2, intervalY / 2 - heiA / 2
targetA = np.array([[0, 0], [0, heiA], [lenA, heiA], [lenA, 0]], dtype=float)
targetA[:, 0] += x0A
targetA[:, 1] += y0A
polygonA = Polygon(targetA)
targetarea = PolyArea(polygonA)

drawpoly(polygonA, ax, clr='g', al=1)

xpoleB = intervalX * np.random.rand(1, n)
ypoleB = intervalY * np.random.rand(1, n)
allpoints = DropPoleB(n, xpoleB, ypoleB, heiB=heiB, lenB=lenB)
polygons = [Polygon(polypoints) for polypoints in allpoints]
# [drawpoly(polygon,ax) for polygon in polygons]
hits = [polygonA.intersection(polygon) for polygon in polygons]
damagemap = [hit for hit in hits if hit.geom_type == 'Polygon']

try:
    unionarea = damagemap[0]
except IndexError:
    print('There is no damage to target!')
else:
    ratio = np.array([area.area / polearea for area in damagemap])
    unionarea = cascaded_union(damagemap)
    drawpoly(unionarea, ax, clr='r', al=.9)
    ratio = np.append(ratio.round(1), np.zeros(len(polygons) - len(damagemap)))
    uni, counts = np.unique(ratio, return_counts=True)
    a = dict(zip(uni, counts))
    plt.figure()
    plt.bar(list(a.keys()), np.array(list(a.values())) / n, width=.1)

ax.set_xlim([0, intervalX])
ax.set_ylim([0, intervalY])
plt.show()