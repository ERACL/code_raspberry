from multiprocessing import Queue
import time

q = Queue()

for i in range(5):
    q.put(i)
time.sleep(3)
while not q.empty():
    print (q.get())
