import threading


class test(threading.Thread):
    def run(self):
        for _ in range(1000):
            tmp=1
            for i  in range(100):
                tmp=i*tmp
            print(threading.current_thread().getName())


x = test(name='im x')
y = test(name='im y')

x.start()
y.start()
