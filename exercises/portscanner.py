# threaded port scanner

import socket
import threading
from queue import Queue

print_lock = threading.Lock()
server = 'pythonprogramming.com'


def pscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((server, port))
        with print_lock:
            print('port {} is open---------via thread {}'.format(port, threading.current_thread().name))
        s.close()
    except:
        with print_lock:
            print('port {} is close via thread {}'.format(port, threading.current_thread().name))


def threader():
    while True:
        worker = q.get()
        pscan(worker)
        q.task_done()


q = Queue()

for x in range(10):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for y in range(1, 101):
    q.put(y)

q.join()
