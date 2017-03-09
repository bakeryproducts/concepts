# Polygon from matplotlib and Area
import numpy as np
import matplotlib.pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import Polygon

def PolyArea(poly):
    x,y = poly.exterior.xy
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def DropPoleB(x0, y0, *, heiB=1., lenB=2.):
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
n = 10000
intervalX, intervalY = 20, 15
lenA, heiA = 8, 4

x0A, y0A = intervalX / 2 - lenA / 2, intervalY / 2 - heiA / 2
targetA = np.array([[0, 0], [0, heiA], [lenA, heiA], [lenA, 0]], dtype=float)
targetA[:, 0] += x0A
targetA[:, 1] += y0A
polygonA = Polygon(targetA)
targetarea=PolyArea(polygonA)
polearea=2
print('Area of target is {}'.format(targetarea))
drawpoly(polygonA, ax, clr='g', al=1)

for _ in range(n):
    xpoleB, ypoleB = intervalX * np.random.rand(), intervalY * np.random.rand()
    polygonB = Polygon(DropPoleB(xpoleB, ypoleB,heiB=1,lenB=2))
    polygons.append(polygonB)
    #drawpoly(polygonB, ax, al=.4)

hits = [polygonA.intersection(poly) for poly in polygons]
damagemap = [hit for hit in hits if hit.geom_type == 'Polygon']
ratio=np.zeros(len(polygons)-len(damagemap))
try:
    unionarea = damagemap[0]
except IndexError:
    print('There is no damage to target!')
else:

    for area in damagemap:
        unionarea = area.union(unionarea)
        ratio=np.append(ratio,area.area/polearea)
    drawpoly(unionarea, ax, clr='r', al=.9)
    totalarea=0
    stot=0
    try:
        for area in unionarea:
            totalarea+=PolyArea(area)
            stot+=area.area
            #print(area.area)
    except TypeError:
        totalarea=PolyArea(unionarea)
        stot = unionarea.area
    print('Damaged area is {:.5f} ({:.5f})\npercentage: {:.3f} %'.format(
        totalarea,stot,100 - 100 * (targetarea - totalarea) / targetarea))


ratio=ratio.round(decimals=1)

uni,counts = np.unique(ratio,return_counts=True)
a=dict(zip(uni,counts))

print(a)

ax.set_xlim([0, intervalX])
ax.set_ylim([0, intervalY])

plt.figure()
plt.bar(list(a.keys()),list(a.values()),width=.1)


plt.show()
