# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'


# 在 cpython 中垃圾回收的算法： 引用计数

a = object()
b = a

del a
try:
	print(b)
	print(a)
except Exception as e:
	print(e)

""":return
<object object at 0x7f49c47e60d0>
name 'a' is not defined
"""


class A:
	def __del__(self):
		pass
