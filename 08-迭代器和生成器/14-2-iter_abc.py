# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'

# 可迭代的对象和迭代器之间的关系:Python 从可迭代的对象中获取迭代器

c = 'abc'
for n in c:
	print(n)


it = iter(c)

while True:
	try:
		print(next(it))
	except StopIteration as e:
		del it
		break

"""
➊ 使用可迭代的对象构建迭代器 it。
➋ 不断在迭代器上调用 next 函数，获取下一个字符。
➌ 如果没有字符了，迭代器会抛出 StopIteration 异常。 
➍ 释放对 it 的引用，即废弃迭代器对象。
➎ 退出循环。
"""

"""
ll = [n for n in range(10)]
ll
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
it = iter(ll)
type(it)
<class 'list_iterator'>
it
<list_iterator object at 0x7f721297f780>
next(it)
"""