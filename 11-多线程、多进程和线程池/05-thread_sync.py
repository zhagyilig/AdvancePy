# -*- encoding: utf-8 -*-
'''
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-11-23 19:55
@Desc    :  线程同步: Lock Rlock
@Docs    :
'''


import threading
from threading import Lock, RLock

# 加锁代码交替运行，用锁会影响性能
# 锁是引起死锁

# 如果使用：RLock， 那么在同一个线程里面，可以连续调用多次acquire， 一定要注意acquire的次数要和release的次数相等


total = 0
# lock = Lock()
lock = RLock()

def add():
    global total
    global lock
    for n in range(1000):
        lock.acquire()  # 获得锁
        lock.acquire()  # 会出现死锁
        total += 1
        lock.release() # 释放锁
        lock.release() # 释放锁

def desc():
    global total
    global lock
    for n in range(100000):
        lock.acquire()
        total -+ 1
        lock.release()

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)
