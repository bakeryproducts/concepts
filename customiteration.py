class Skiptwo:
    def __init__(self, word):
        self.data = word
        self.index = -1

    def __iter__(self):
        return self

    def next(self):
        if self.index >= len(self.data) - 2:
            raise StopIteration
        else:
            self.index += 2
            return self.data[self.index]


test = Skiptwo('Aroused by your greatness')
for i in test:
    print(i)

# ------------------------------------------
mx = lambda x, y: x if x > y else y

print(mx(10, 13))

# ------------------------------------------

import math

li = [4, 9, 16, 24, 36, 40]

print(list(map(lambda x: math.sqrt(x), li)))

# ----------------------------------------------
print(list(filter(lambda x: x < 25, li)))
print(list(map(lambda x: x < 25, li)))

# ----------------------------------------------
#----[a,b,c,d] f(list) = f(f(a,b,c),d)...-----
prod = reduce(lambda x, y: x * y, li)
print(prod)

#----------------------------------------------

print ('{} and {}'.format((1,2),[0]))

#---fib-------------------------------------------

a,b = 0,1
for _ in range(10):
    a,b = b,a+b
    print (b)

