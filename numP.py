#   basically numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a * b)
print(a.dot(b))
print(a / b)
print(np.sin(a))

c = np.linspace(0, 2 * np.pi, 50)  # linear set of numbers for [0,2Pi] 50 elements (?)

# plt.plot(c, np.sin(c), 'b-o',
#          c, np.sin(2 * c), 'r-^', label=['sin2','cos'])  # two graphics on same plot, 'Blue solid with o'
# plt.legend()
#plt.legend(['sin','cos'])
# plt.scatter(c,np.sin(c))

x = np.random.rand(200)  # random value from 0,1  x200
y = np.random.rand(200)
size = np.random.rand(200) * 40  # scale 40
col = np.random.rand(200)

plt.figure()
plt.subplot(2, 1, 1)  # subplot(2 - rows, 1 - columns,1 - active,  used to draw now)
plt.scatter(x, y, size, col, cmap='jet')  # coors, size , color, colormap='
plt.colorbar()
# hold(False)

plt.figure()
#plt.close('all')

plt.show()
