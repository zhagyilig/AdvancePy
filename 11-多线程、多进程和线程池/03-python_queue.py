# -*- encoding: utf-8 -*-
'''
@Author  :   ericzhang
@Version :   python3.6
@File    :   03-python_queue.py
@Time    :   2019/11/23 08:08:28
@Desc    :   线程间的通信：共享变量和 queue, 这个脚本是共享变量
@Docs    :
'''


import time
import threading

# 抓取文章列表url的存放地址，然后 get_detail_html 方法读取url
detail_url_list = []


def get_detail_html():
    """抓取详情页."""
    global detail_url_list

    while True:
      if len(detail_url_list) > 0:
          print('-----------------')
          url = detail_url_list.pop()
          print('url: ' + url)
          print("get detail html started")
          time.sleep(5)
          print("get detail html end")


def get_detail_url():
    """抓取文章列表页."""
    global detail_url_list
    while True:
        for n in range(5):
            print('+++++++++++++')
            print("get detail url started")
            detail_url_list.append('https://kk.net/{}'.format(n))
            time.sleep(4)
            print("get detail url end")
        print(detail_url_list)



#1. 线程通信方式 - 共享变量


if __name__ == '__main__':
    url_thread = threading.Thread(target=get_detail_url)
    url_thread.start()
    for n in range(10):
        html_thread = threading.Thread(target=get_detail_html)
        html_thread.start()