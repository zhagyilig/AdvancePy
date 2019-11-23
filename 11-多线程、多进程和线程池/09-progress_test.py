# -*- encoding: utf-8 -*-
'''
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-11-23 23:36
@Desc    :  多进程编程
@Docs    : 
'''


import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# 多进程编程：
# 消耗cpu的操作，用多进程；对于多io操作，使用多线程编程，进程切换代价要高于线程

# 下面的脚本就是测试进程和线程耗时
####  1. 对于消耗cpu操作，多进程优于多线程 ####

def fab(n):
    if n <= 2:
        return 1
    return fab(n-1) + fab(n-2)

if __name__ == '__main__':
    pass
    # 多线程
    # with ThreadPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fab, (num)) for num in  range(20, 35)]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print('exec result: {}'.format(time.time() - start_time))
    #     print('last result: {}'.format(time.time() - start_time))
          # last result: 7.193867921829224

    # with ProcessPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fab, (num)) for num in  range(20, 35)]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print('exec result: {}'.format(time.time() - start_time))
    #     print('last result: {}'.format(time.time() - start_time))
        # last result: 4.979384899139404


####  1. 对于io操作来说，多线程优于多进程 ####
def random_time(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    # 多线程
    # with ThreadPoolExecutor(3) as executor:
    #     all_task = [executor.submit(random_time, (num)) for num in [2]*20]
    #     start_time = time.time()
    #     for future in  as_completed(all_task):
    #         data = future.result()
    #         print("exe result: {}".format(data))
    #     print("last time is: {}".format(time.time() - start_time))
    #     # last time is: 14.024287223815918


    #  多进程
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_time, (num)) for num in [2]*20]
        start_time = time.time()
        for future in  as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))
        print("last time is: {}".format(time.time() - start_time))
