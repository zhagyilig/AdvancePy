# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-29 10:47
@Desc    :            
@Docs    : 
"""

# immutable 不可变对象


from collections import namedtuple


class User:
	def __init__(self, name, age):
		self.name = name
		self.age = age


user = User(name='eric', age=22)
print(user.name, user.age)  # 取tpuple中的值


# 创建一个 user 的类
user = namedtuple('User', ['name', 'age'])



user  = namedtuple('User', ['name', 'age'])


import requests