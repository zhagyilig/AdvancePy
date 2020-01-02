# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'

"""
可迭代的对象一定不能是自身的迭代器。也就是说，可迭代的对象必须实现 __iter__ 方法，但不能实现 __next__ 方法。
另一方面，迭代器应该一直可以迭代。迭代器的 __iter__ 方法应该返回自身。
"""


import re
import reprlib
from collections.abc import  Iterator

RE_ROWD = re.compile('\w+')

class Sentence:
	def __init__(self, text):
		self.text  = text
		self.words = RE_ROWD.findall(text)

	def __repr__(self):
		return 'Sentence(%s)' % reprlib.repr(self.text)

	def __iter__(self):
		""" 根据可迭代协议，__iter__ 方法实例化并返回一个迭代器。 """
		return SentenceIterator(self.words)


class SentenceIterator(Iterator):
	def __init__(self, words):
		self.words = words
		self.index = 0

	def __next__(self):
		try:
			word = self.words[self.index]
		except IndexError:
			raise StopIteration()
		self.index += 1
		return word


	# 如果继承了 Iterator, 可以不用 __iter__
	# def __iter__(self):
	# 	return self  #  返回实例本身(返回迭代器本身)

if __name__ == '__main__':
    s = Sentence('"the time has come," the Walrus said.')
    for n in s:
	    print(n)
    print(list(s))

""":return
the
time
has
come
the
Walrus
said
['the', 'time', 'has', 'come', 'the', 'Walrus', 'said']
"""

"""
➊ 与14-1相比，这里只多了一个 __iter__ 方法。这一版没有 __getitem__ 方法，为的是 明确表明这个类可以迭代，因为实现了 __iter__ 方法。
➋ 根据可迭代协议，__iter__ 方法实例化并返回一个迭代器。 
➌ SentenceIterator 实例引用单词列表。
➍ self.index 用于确定下一个要获取的单词。
➎ 获取 self.index 索引位上的单词。
➏ 如果 self.index 索引位上没有单词，那么抛出 StopIteration 异常。 ➐ 递增 self.index 的值。
➑ 返回单词。
➒ 实现 self.__iter__ 方法。
"""

###############

from collections.abc import Iterator


class UserList:
	def __init__(self, user_list):
		self.user_list = user_list

	def __iter__(self):
		return UserListIterator(self.user_list)

class UserListIterator(Iterator):
	def __init__(self, user_list):
		self.user_list = user_list
		self.index = 0

	def __next__(self):
		try:
			user = self.user_list[self.index]
		except IndexError:
			raise StopIteration
		self.index += 1
		return user

if __name__ == '__main__':
	user_list = [user for user in range(8)]
	users = UserList(user_list)
	for n in users:
		print(n)