import time
import random


def foo1(a):
    maxmult = 0
    for i in range(len(a) - maxlen + 1):
        li = a[i:i + maxlen]
        currmult = 1
        for sym in li:
            currmult *= int(sym)
            # print(sym, end=' * ')
        # print(' = ' + str(currmult))
        if currmult > maxmult:
            maxmult = currmult
    return maxmult


def foo2(a):
    maxmult = 0
    currmult = 1
    ind = 0
    for sym in a:
        if ind < maxlen:
            currmult *= int(sym)
        else:
            currmult *= int(sym)
            currmult /= int(a[ind - maxlen])

        if currmult > maxmult:
            maxmult = currmult
        ind += 1
    return maxmult


inp = ''.join([str(random.randrange(1, 10)) for n in range(9000)])
#print(inp)
maxlen = 100

start = time.time()
res = foo1(inp)
restime1=time.time()-start
print('worked like a charm in {}'.format(restime1))
#print('Maximum prodcution is {}'.format(res))

start = time.time()
res = foo2(inp)
restime2=time.time()-start

print('worked like a charm in {}'.format(restime2))
#print('Maximum prodcution is {}'.format(res))

print('better in {} times'.format(restime1/restime2))