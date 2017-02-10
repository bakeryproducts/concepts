import random
li = [1,2,3]

def dbl(amm):
    return amm*2

new = list(map(dbl,li))
print(new)

#---------------------------------------
import heapq

ran=[random.randint(1,100) for _ in range(10)]

print(heapq.nlargest(3,ran),ran)



# 2/12/2013 9/2/2017
month=3
year=3
