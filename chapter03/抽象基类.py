# -*- encoding: utf-8 -*-
'''
@Author  :   ericzhang 
@Version :   python3.6
@File    :   抽象基类.py
@Time    :   2019/11/10 15:45:39
@Desc    :            
@Docs    :            
'''


# 1、 我们去检查某一个类是否有某一个方法
class Company(object):
    def __init__(self, *args, **kwargs):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def say(self):
        return 'i love python.'


employee_list = ['eric1', 'eric2', 'eric3']
com = Company(employee_list)

print(hasattr(com, '__len__'))

# 2、我们在某些情况之下希望判定某个对象的类型

from collections.abc import Sized
print(isinstance(com, Sized))

# 3、我们需要强制某个子类必须实现某些方法
#实现了一个web框架，集成cache(redis, cache, memorychache)
#需要设计一个抽象基类， 指定子类必须实现某些方法

# 如何去模拟一个抽象基类
import abc
from collections.abc import *


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass
# class CacheBase():
#     def get(self, key):
#         raise NotImplementedError
#     def set(self, key, value):
#         raise NotImplementedError
#
class RedisCache(CacheBase):
    def set(self, key, value):
        pass

# redis_cache = RedisCache()
# redis_cache.set("key", "value")
