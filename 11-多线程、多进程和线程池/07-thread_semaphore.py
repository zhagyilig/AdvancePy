# -*- encoding: utf-8 -*-
'''
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-11-23 22:19
@Desc    :  Semaphore(信号量) 是用于控制进入数量的锁
@Docs    :
'''

#文件， 读、写， 写一般只是用于一个线程写，读可以允许有多个

## 脚本功能
#做爬虫: 限制爬取网页的并发数量


import threading
import time

class HtmlSpider(threading.Thread):
    """get html."""
    def __init__(self, url, sem):
        super(HtmlSpider, self).__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release() # 释放锁

class UrlProducer(threading.Thread):
    """get url"""
    def __init__(self, sem):
        super(UrlProducer, self).__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()  # 获取锁
            html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
            html_thread.start()

if __name__ == "__main__":
    sem = threading.Semaphore(3)  # 一次限制 3 个并发
    url_producer = UrlProducer(sem)
    url_producer.start()
