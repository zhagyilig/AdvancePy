# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'

"""
只要 Python 函数的定义体中有 yield 关键字，该函数就是生成器函数
"""

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)

	def __repr__(self):
		return 'Sentence(%s)' % reprlib.repr(self.text)

	def __iter__(self):
		# __iter__ 方法是生成器函数，调用时会构建一个实现了迭代器接口的生成器对象
		for word in self.words:
			yield word
		# return word
		# 在Python3.3之前，如果生成器函数中的return 语句有返回值，那么会报错。现在可以这么做，不过return 语句仍会导致
		# StopIteration 异常抛出。调用方可以从异常对象中获取返回值。可是，只有把生成器函数当成协程使用时，这么做才有意义

if __name__ == '__main__':
    s = Sentence('"the time has come," the Walrus said.')
    print(type(s))  # <class '__main__.Sentence'>
    for n in s:
	    print(n)
"""
➊ 迭代 self.words。
➋ 产出当前的 word。
➌ 这个 return 语句不是必要的;这个函数可以直接“落空”，自动返回。不管有没有
return 语句，生成器函数都不会抛出 StopIteration 异常，而是在生成完全部值之后会
直接退出。
➍ 不用再单独定义一个迭代器类!
"""


### 可迭代对象不是迭代器，迭代器是可迭代对象，生成器是迭代器