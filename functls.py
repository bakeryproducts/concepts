import functools

#@functools.lru_cache(maxsize=64)       # memoized for naturalov

f = functools.partial(sorted,key=lambda p: p[1]) # fix arg #2
print(f([('a',2),('b',1)]))



