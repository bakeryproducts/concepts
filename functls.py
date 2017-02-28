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

xs = {1,2,3}
ys = {1,2,3,4,5}
print(xs < ys)              # | is union & is intersection

ys.remove(3)
ys.discard(999)             # ys.remove will raise, discard will not
print(ys)

d = {'abcd':'foo','var':'bar'}
d.setdefault('nkey','newvalue')          # set value if key not exist
print(d.get('abcd',42))                 # returns value if exist, or 42
print(d.pop("nkey"),d)

from collections import defaultdict
g = defaultdict(set,**{'a':{'b'}})      # def dict allows to .add new keys
g['a'].add('c')
g['who']={5}
g['newkey'].add('newvalue')
print(g)

from collections import Counter

c = Counter(['foo','foo','bar'])
d=Counter('abcaabe')
c['foo']+=1
print(d,c)