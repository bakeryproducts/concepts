# wrapping 101
def add_wrap(item):
    def wrap_item():
        return 'box for {}'.format(str(item()))

    return wrap_item


@add_wrap
def foo():
    return 'im foo'


@add_wrap
@add_wrap
def moo():
    return 'im moo'


print(foo(), '\n', moo())

from functools import wraps


def style_wrap(addstyle):
    def add_wrap(func_item):
        return '{} box for {}'.format(addstyle, func_item())

    return add_wrap


@style_wrap(' big ')
def goo():
    return 'im goo'


print('\n' * 10)
# --------------------------------------------------------------
# 22/02/17 more on wrapping
import sys
import time

trace_enabled = True


def trace(func=None, *, handle=sys.stdout):
    if func is None:
        # print('func is none!')
        return lambda func: trace(func, handle=handle)

    @wraps(func)
    def inner(*args, **kwargs):
        print('im wrapper for {} func, args: {}, kwargs: {}'.format(func.__name__, args, kwargs))
        return func(*args, **kwargs)

    return inner if trace_enabled else func


@trace(handle=sys.stderr)
def identity(x):
    'i do nothing'
    return x


# print(identity(42))
# identity = trace(identity)
# print(identity(42))


# print(identity.__doc__)
# -----------------timethis-----------

def timethis(func=None, *, handle_iter=10):
    if func is None:
        return lambda func: timethis(func, handle_iter=handle_iter)

    @wraps(func)
    def inner(*args, **kwargs):
        min_time = float('inf')
        for i in range(handle_iter):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            min_time = min(min_time, time.perf_counter() - start)

        print('minimal time is {} s'.format(min_time))

        return result

    return inner


@timethis
def exmp(x):
    return sum(range(x))


#
# print(exmp(10 ** 6))
# print(timethis(sum, handle_iter=5)(range(10 ** 6)))

def memoized(func):  # cache func res , speedup
    cache = {}

    @wraps(func)
    def inner(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return inner


@memoized
@timethis
def exmp2(x):
    return sum(range(x))


#
# start=time.perf_counter()
# print('res is {}, worked for {} s'.format(memoized(exmp)(10**7),time.perf_counter()-start))
# start=time.perf_counter()
# print('res is {}, worked for {} s'.format(memoized(exmp)(10**7),time.perf_counter()-start))
#
# print(exmp2(10**7))
# print(exmp2(10**7))
# print(exmp2(10**6))
# print(exmp2(10**6))
#

def squ(func):
    return lambda x: func(x * x)


def adds(func):
    return lambda x: func(x + 1)


@adds                   # order of decorators matter!
@squ                    # ex3 = adds(squ(ex3)
def ex3(x):
    return x

print(ex3(2))
# print(squ(range)(2))

