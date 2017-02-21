# func min
import random


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


print(bounded_min(*get_ls(), lo=7,hi=17))
