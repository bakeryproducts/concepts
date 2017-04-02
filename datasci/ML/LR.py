import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from statistics import mean


# y = kx+b

def ar(n, k, b, sko):
    xs = np.arange(n, dtype='float64')
    ys = []
    for i in range(n):
        y = k * xs[i] + b + random.randint(-sko, sko) / 10
        ys.append(y)
    return xs, ys


def lr(xs, ys):
    x = np.mean(xs)
    y = np.mean(ys)
    m = (x * y - np.mean(xs * ys)) / (x ** 2 - np.mean(xs * xs))
    b = y - m * x
    return m, b


def sqerror(y_o, y_l):
    return sum((y_l - y_o) ** 2)


def r2(y_orig, y_line):
    y_mean_line = np.array([np.mean(y_orig) for y in y_orig])
    print(type(y_line))
    print(type(y_orig))
    sqer_regr = sqerror(y_orig, y_line)
    sqer_mean = sqerror(y_mean_line, y_orig)
    coef = 1 - (sqer_regr / sqer_mean)
    return coef


X, Y = ar(30, .3, 5, 10)

k, b = lr(X, Y)
rl = k * X + b

r2coef = r2(Y, rl)
print(r2coef)


plt.scatter(X, Y)
plt.plot(X, k * X + b)
# plt.plot([X[0],X[-1]],[rl[0],rl[-1]])

plt.show()
