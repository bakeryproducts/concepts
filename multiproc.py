import multiprocessing
from multiprocessing import Pool


def checker(num):
    print('im {}'.format(num))
    return 2*num


def foo1():
    for i in range(20):
        p = multiprocessing.Process(target=checker, args=(i,))
        p.start()
        # p.join()

def foo2():
    p = Pool(processes=10)
    data = p.map(checker,range(10))
    p.close()
    print(data)
if __name__ == '__main__':
    # foo1()
    foo2()
