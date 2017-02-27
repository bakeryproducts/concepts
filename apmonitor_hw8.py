#numpy basic matrix operations

import numpy as np
import random

#x = np.ones(50)

y = np.linspace(1, 20, 50)
z = np.zeros(50)

for i in range(50):
    z[i] = (i) * 19 / 49 + 1

# print(z)
print()
# print(np.sum(abs(z-y)))

m = np.ones(30)
# m.shape=(1,1)
for i in range(30):
    m[i] = random.randrange(10)

print(m)
print(m.mean())

a = np.random.randint(1, 10, size=30)

a = a.reshape([5, 6])

for i in np.arange(np.size(a, 0)):
    for j in np.arange(np.size(a, 1)):
        if a[i, j] == 5:
            print(i, j)

# print(a)


a = np.arange(1, 9 + 1).reshape((3,3))
b=np.array([[-.1,-.2,-.3]
           ,[3,10,2],
            [4,2,.5]])
x = np.array([[1, 3, 4]])           # do double [[ for later transposing
x=x.T                               # like that

print(np.dot(a,b))                  # two variants (works frequently for many operations)
print(a.dot(b))
print(np.cross(a,b))                # x product
print(a.dot(x))

np.linalg.inv(a)                    # from lin algebra :inverse A, A^-1

