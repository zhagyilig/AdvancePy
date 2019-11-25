# -*- encoding: utf-8 -*-
'''
@Author  :   ericzhang
@Version :   python3.6
@File    :   03-python_queue.py
@Time    :   2019/11/23 08:08:28
@Desc    :   线程间的通信：共享变量和 queue, 这个脚本是 queue
@Docs    :
'''

import time
import threading
from queue import Queue


def get_detail_html(queue):
    """get html"""
    while True:
        time.sleep(5)
        print('+++ start get html +++')
        url_result = queue.get()
        print(222, url_result)


def get_detail_url(queue):
    """get url"""
    while True:
        time.sleep(5)
        print('--- start get url ---')
        for n in range(10):
            queue.put('https://xtrdb.net/{}'.format(n))


if __name__ == '__main__':
    thread_queue = Queue(maxsize=1000)
    get_url_thread = threading.Thread(target=get_detail_url, args=(thread_queue,))
    get_url_thread.start()
    for thread in range(2):
        get_html_thread = threading.Thread(target=get_detail_html, args=(thread_queue,))
        get_html_thread.start()