# Queues basics FIFO LIFO

from queue import Queue

# from queue import LifoQueue

q = Queue()  # FIFO don forget bracers!
# q2 = LifoQueue()               #LIFO

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())  # get() returns value and pops it

# Also there is Priority Queue

from queue import PriorityQueue

pq = PriorityQueue()

pq.put((10, 'studying'))  # number is importance
pq.put((1, 'lay down'))
pq.put((2, 'eat'))

while not pq.empty():
    print(pq.get()[1])  # returns tuple so [1] for task

# ALSO there is a Deque: double ended queue

from collections import deque

dq = deque('this is a test')
print(dq)

for i in dq:
    print(i)

print(dq.count('t'))

dq.extend(' and this is more of it')        # adds to the right
dq.extendleft(' smthing')
dq.pop()
dq.popleft()
dq.remove('m')
dq.rotate(4)
print(''.join(dq))

