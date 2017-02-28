import functools

#@functools.lru_cache(maxsize=64)       # memoized for naturalov

f = functools.partial(sorted,key=lambda p: p[1]) # fix arg #2
#print(f([('a',2),('b',1)]))

from collections import deque
import numpy
x=range(10)


a = deque(x,maxlen=4)
a.extend([1,1])
a.popleft()
a.extendleft([8,8])
print(a)


