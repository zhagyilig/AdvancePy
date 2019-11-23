# -*- encoding: utf-8 -*-
'''
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-11-23 23:12
@Desc    :            
@Docs    : 
'''

import time
from concurrent import futures # 这是包是专门做线程池和进程池编程，接口几乎一一致 # python3.2之后
from concurrent.futures import as_completed, ThreadPoolExecutor

# 为什么需要线程池?

# futures功能:
# 做线程数量的控制
# 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候我们主线程能立即知道
# futures可以让多线程和多进程编码接口一致

def get_html(times):
    time.sleep(times)
    print('get page {} success'.format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
# max_workers: 线程数量

# 通过submit函数提交执行的函数到线程池中，submit 是提交即返回 -> 非阻塞io
task1 = executor.submit(get_html, (3))
task1 = executor.submit(get_html, (2))

# task1 是一个对象，它常用的方法： 判断某一个任务是否完成:done 执行结果: result 取消线程: cancel
print(task1.done())
print(task1.cancel())

time.sleep(2)

# result 方法获取task的执行结果
print(task1.result())

print(22222222222222222)
## 2. 上面的 task1 task2 ... 是单个提交并且只能获取单个任务的返回，下面优化: 批量提交和获取已经成功的task返回

urls = [1,2,3,5]

# 批量提交
all_task = [executor.submit(get_html, (url)) for url in  urls]
for future in as_completed(all_task):
    # 返回所有已经执行成功的任务 异步操作
    data = future.result()
    print('get {} page success.'.format(data))

print(33333333333)
# 通过executor的map获取task的执行结果的值，是上面的简单写法。
for data in executor.map(get_html, urls):
    print("get {} page".format(data))


## 总结:
from concurrent.futures import Future # 未来函数也是线程执行后数据的容器，学习它的设计理念，很重要！