import numpy as np
import random

x = np.ones(50)

y = np.linspace(1, 20, 50)
z=np.zeros(50)

for i in range(50):
    z[i] = (i) * 19/49+1


print(z)
print()
print(np.sum(abs(z-y)))

m=np.ones(1)
#m.shape=(1,1)
i=0
while m[-1] != 7 and i<=30:
    m = np.append(m, random.randrange(1,10))
    i+=1

print(m)
print(m.mean())
