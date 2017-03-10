# basics of threading with queues 
import threading
from queue import Queue
import time

print_lock = threading.Lock()       #lock for continues printing

def job(worker):                    #main job to be done with multiple threads
    time.sleep(.5)                  #sim it
    with print_lock:
        print(threading.current_thread().name,worker) # print out name of current thread

def threader():                     # func that will take workers from Q
    while True:                     # because there are 10 threads for 20 workers
        worker = q.get()            # pop worker from Q
        job(worker)                 # assign job to worker
        q.task_done()               # ??

q = Queue()

for x in range(10):                             #creating 10 threads for threader func
    t = threading.Thread(target=threader)
    t.daemon = True                             # making it daemons for proper quit (?)
    t.start()

print(threading.active_count())

starttime = time.time()

for worker in range(20):
    q.put(worker)                               # fill Q with workers

q.join()                                        # ???

print('Job took: {}'.format(time.time() - starttime))


#threading commands
# print(threading.active_count())
# print(threading.enumerate())
# my_thread.is_alive()
# my_thread.join() waits thread to finish before starting another

def my_foo():
    print('im foo from my_thread!')

my_thread = threading.Thread(target=my_foo(),name='Mythread')
my_thread.start()
