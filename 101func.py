# func min
import random
import dis


def get_ls():
    ls = [random.randrange(1, 20) for _ in range(10)]
    print(ls)
    return ls


def mmin(first, *args):
    res = first
    for arg in args:
        if arg < res:
            res = arg
    return res


ls1 = {-5, 10, 0, 12}
ls2 = [-1, 0, 2, 3, 5]
ls3 = (0, 2, 1, 23)
lss = [ls1, ls2, ls3]

for ls in lss:
    print(mmin(*ls))  # unpack!


def bounded_min(first, *args, lo=float('-inf'), hi=float('inf')):
    res = hi
    for arg in (first,) + args:
        if arg < res and lo < arg < hi:
            res = arg
    return max(res, lo)


print(bounded_min(*get_ls(), lo=7, hi=17))


def unique(iter, seen=None):  # seen = set() works only one time  - bytecode
    seen = set(seen or [])  # so double unique will return []; None -> Falsy
    acc = []  # do not do this
    for item in iter:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc


ls = get_ls()
print(unique(ls))
print(unique(ls))
print(ls)


def flatten(xs, *, depth=None):
    pass


flatten(1, depth=2)  # only depth= usage

first, *rest, last = range(5)
print(first, rest, last)

for a, *b in [range(4), range(2)]:  # for each el in [[],[]] take a= first and b = rest
    print(b)

dis.dis('first,*rest,last = (1,2,3)')


def wrapper():
    def identity(x):
        print('im id')
        return x

    def dedentity(y):
        print('im de')
        return y

    return dedentity


f = wrapper()
print(f('bro'))


def make_min(*, lo, hi):
    def inner(first, *rest):
        res = hi
        for arg in (first,) + rest:
            if arg < res and lo < arg < hi:
                res = arg
        return max(res, lo)

    return inner


boundmin = make_min(lo=3, hi=10)
print(boundmin(*get_ls()))


def cell(val=None):
    def get():
        return val

    def set(upd):
        nonlocal val
        val = upd

    return get, set


ge, se = cell(13)
print(ge(), se(69), ge())
print(ge())
