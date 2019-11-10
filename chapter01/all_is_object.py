# coding=utf-8

'''
@Author  : ericzhang
@Version : python3.7
@Date    : 2018-08-10 08:05
@Soft    : PyCharm
@Desc    : python中一切皆对象
@Docs    : 
'''


## 1、赋值给一个变量
def myFunc(name='jiading'):
    print(name)

my_fun = myFunc # 赋值
my_fun('pudong')

class Person:
    def __init__(self):
        print('changning')

my_class = Person
my_class()

"""
pudong
changning
"""


## 2、可以添加到集合对象中
obj_list = []

obj_list.append(my_fun)
obj_list.append(my_class)

for item in obj_list:
    print(item())

    """
    zhang
    None
    changning
    <__main__.Person object at 0x101f8f290>
    """

## 3、可以当作函数的返回值
def decotator():
    print('dec start...')
    return my_fun

my_dec = decotator()
my_dec()

"""
dec start...
zhang
"""