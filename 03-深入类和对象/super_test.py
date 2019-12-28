# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-28 14:36
@Desc    :            
@Docs    : 
"""


# super().__init__() 不是调用父类的构造函数，而是根据mro顺序调用
# MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表

class A():
	def __init__(self):
		print('A')


class B(A):
	def __init__(self):
		print('B')
		super(B, self).__init__()

if __name__ == '__main__':
    b = B()
    print(b)