#   basically numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a * b)
print(a.dot(b))             # dot production
print(a / b)
print(np.sin(a))

c = np.linspace(0, 2 * np.pi, 50)  # linear set of numbers for [0,2Pi] 50 elements (?)

# plt.plot(c, np.sin(c), 'b-o',
#          c, np.sin(2 * c), 'r-^', label=['sin2','cos'])  # two graphics on same plot, 'Blue solid with o'
# plt.legend()
# plt.legend(['sin','cos'])
# plt.scatter(c,np.sin(c))

x = np.random.rand(200)  # random value from 0,1  x200
y = np.random.rand(200)
size = np.random.rand(200) * 40  # scale 40
col = np.random.rand(200)

plt.figure()
plt.subplot(2, 1, 1)  # subplot(2 - rows, 1 - columns,1 - active,  used to draw now)
plt.scatter(x, y, size, col, cmap='jet')  # coors, size , color, colormap='
plt.colorbar()
# hold(False)           # look it up!

# plt.figure()
# plt.close('all')

# plt.show()
# plt.savefig('test.png')#,bbox_inches='tight')

a.fill(0)  # fill with 0, faster then a[:]=0
print(a)
a = np.zeros(5)
print(a)

# lets calculate derivative of Sin(x), shall we?------------------------
# hell with it let do integration also
plt.close('all')
a = np.linspace(0, 2 * np.pi, 100)
b = np.sin(a)

dx = a[1:] - a[:-1]
dy = b[1:] - b[:-1]
der = dy / dx

avg_h = (b[1:] + b[:-1]) / 2.
integ = np.cumsum(dx * avg_h)

plt.subplot(1, 2, 1)
plt.plot(a[1:], der, 'rx', a, np.cos(a), 'b-')
plt.title(r"$\rm{Derivative\ of}\ sin(x)$")  # LaTeX mthfckers!!

plt.subplot(1, 2, 2)
plt.plot(a[1:], integ, 'rx', a, np.cos(0) - np.cos(a), 'b-')
plt.title(r'$\int \, \sin(x) \, dx$')  # oh my that int sign!

plt.legend(['numeric', 'actual'])

# plt.show()
# -------------------------------------------------------------------
# array of given size: reshape
r = np.arange(6).reshape(2, 3)
print(r, r[-1, -1])

r = np.arange(30).reshape(5, 6)
print(r % 3 == 0)  # mask for next line: select all elements %3==0
print(r[r % 3 == 0])
r[r % 3 == 0] = -11
# print (np.where(r%3==0))            # returns tuple of indexes which in pairs get r[i,j] that matches condition
r[3, 3] = -27
print(r.argmin())
indc = np.unravel_index(r.argmin(), r.shape)  # returns indexes in multidim array from linear position
print(indc)
