# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-28 17:17
@Desc    :            
@Docs    : 
"""


# 序列的  + += extend 的区别

a = []
a = list()

a = [1, 2]
b = [3, 4]

c = a + b
print(c)

a += [1,2]
print(a)


a.extend(c)
print(a)


# extend 直接赋值, 没有返回值