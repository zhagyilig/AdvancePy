

############
# 什么是迭代协议:
# 1. 可迭代对象：只实现了 __iter__ 方法
# 2. 迭代器： 实现的方法 __iter__  __next__
# 1 2 关系：python 从可迭代的对象中获取迭代器

# 综上, list 就是可迭代对象， 而不是可迭代对象

###########
"""
迭代器
迭代器是这样的对象:实现了无参数的 __next__ 方法，返回序列中的下一个元素;如 果没有元素了，那么抛出 StopIteration 异常。Python 中的迭代器还实现了 __iter__ 方 法，因此迭代器也可以迭代。
因为内置的 iter(...) 函数会对序列做特殊处理，所以第 1 版 Sentence 类可以迭代。接下 来要实现标准的可迭代协议
"""



# https://stackoverflow.com/questions/8009882/how-to-read-a-large-file-line-by-line

from collections.abc import Iterable, Iterator


my_list = [n for n in range(4)]

print(isinstance(my_list, Iterator))
print(isinstance(my_list, Iterable))


""":return
False
True
"""

my_list_iterator = iter(my_list)
print(isinstance(my_list_iterator, Iterator))
print(isinstance(my_list, Iterable))
