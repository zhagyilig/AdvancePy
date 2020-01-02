# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'


import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
	""" 把句子划分为单词序列 """
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)

	def __getitem__(self, index):
		return self.words[index]  # 从 0 开始.

	# def __len__(self):
	# 	return len(self.words)
	#
	# def __repr__(self):
	# 	return 'Sentence(%s)' % reprlib.repr(self.text)

if __name__ == '__main__':
    s = Sentence('"the time has come," the Walrus said.')
    # print(type(s))
    # print(type(iter(s)))
    for n in s:
	    print(n)
    print(list(s))




