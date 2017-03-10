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


a = np.array([1,2,3,4]).reshape(2,2)
b=a
b[0]=13
c=[1,2,3,4]
d=c
d[0]=13

print(c)

a = np.zeros((2,2,3))
print(a)
a=np.ravel(a)                       # flatten
print(a)
print('\n'*10)
twocubes = np.random.randint(1,10,size=8)
subscript = [7,5]                   # can use for a[subscript]
print(twocubes)
#print(twocubes[subscript])
twocubes=twocubes.reshape(2,2,2)
print(twocubes[:,:,0])                     # : means all, i.e. a.shape = 2,2,2
                                    # a[:,:,0] means select all dimensions on level 0
                                    # -> 2x2 matrix  then select all 1D  from them : 1x2
                                    # strings , then look for 0 element

a = np.ones(9,dtype=int).reshape(3,3)
a[1,0]=5
print(a)
print(np.mean(a,0))                 # meam(a,x) gives mean values in axes:
                                    # 0 is 'down' 1 is 'right'
print(twocubes)
print(np.mean(twocubes,2))          # for 3D 0 is 'depth', 1 is 'down' 2 is 'right'
