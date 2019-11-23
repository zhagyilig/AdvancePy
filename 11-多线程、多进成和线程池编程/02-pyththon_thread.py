# -*- encoding: utf-8 -*-
'''
@Author  :   ericzhang
@Version :   python3.6
@File    :   02-pyththon_thread.py
@Time    :   2019/11/23 06:39:36
@Desc    :
@Docs    :
'''


import time
import threading
from threading import Thread

# 对于io操作来说，多线程和多进程性能差别不大

# 1.通过Thread类实例化


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")


if __name__ == '__main__':
    thead1 = threading.Thread(target=get_detail_html, args=('',))
    thead2 = threading.Thread(target=get_detail_url, args=('',))

    start_time = time.time()
    thead1.start()
    thead2.start()

    # This blocks the calling thread # 等待thead1 2 执行完成，才执行print
    thead1.join()
    thead2.join()

    print('last time: {}'.format(time.time() - start_time))

#2. 通过集成Thread来实现多线程
print(2222222222)

class GetDtailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDtailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail url started')
        time.sleep(4)
        print('get detail url end')

if __name__ == "__main__":
    thread1 = GetDtailHtml('get_detail_html')
    thread2 = GetDtailUrl('get_detail_url')
    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


    #当主线程退出的时候， 子线程kill掉
    print ("last time: {}".format(time.time()-start_time))