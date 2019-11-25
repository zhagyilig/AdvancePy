# -*- encoding: utf-8 -*-
'''
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-11-24 11:17
@Desc    :            
@Docs    : 
'''


import os
import time

#fork只能用于linux/unix中
pid = os.fork()


if pid == 0:
    print("ericzhang")
    print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
else:
    print('我是父进程：{}.'.format(pid))
time.sleep(3)
