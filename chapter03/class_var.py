# -*- encoding: utf-8 -*-
'''
@Author  :   ericzhang 
@Version :   python3.6
@File    :   class_var.py
@Time    :   2019/11/10 17:39:44
@Desc    :   类变量和实例变量的区别
@Docs    :
'''

class A:
    aa = 11  # 类变量
    # __init__ 构造函数
    # self 这个类的实例
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(1,2)
print(a.x, a.y, a.aa)