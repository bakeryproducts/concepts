import functools
import time


def timethis(func=None, *, handle_iter=10):
    if (func is None):
        return lambda func: timethis(func, handle_iter=handle_iter)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        for i in range(handle_iter):
            res = func(*args, **kwargs)

        print('done in {:5.5f} s '.format(time.perf_counter() - start), end=' ')
        return res

    return inner


@timethis(handle_iter=10000)
def is_prime(x):
    for d in range(2, x):
        if x % d == 0:
            return False
    return True


# for i in range(10):
#     print('{} is prime: {}'.format(i, is_prime(i)))


def get_dic():
    with open('visitedUrls.txt', 'r') as f:
        res = f.read()
    return res


li = get_dic().split('\n')
dic = {}
for item in li:
    sets = item.split('-')
    for term in sets[1].split(','):
        dic[term] = sets[0]

print(li)
for k, v in dic.items():
    print('{} means {}'.format(k, v))
