# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-28 17:28
@Desc    :            
@Docs    : 
"""

# http://effbot.org/zone/python-with-statement.htm

# 1. 上下文管理器协议

class Sample:
	# 定义一个上下文管理器
	def __enter__(self):
		# 获取资源
		print('enter.')
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		# 释放资源
		print('exit.')

	def do_something(self):
		print('do_something...')

with Sample() as sample:
	sample.do_something()

""":return
enter.
do_something...
exit.
"""


# 2. contextilb简化上下文管理器, 进一步优化 1.

import contextlib

@contextlib.contextmanager
def file_open(file_name):
	print('file open...')
	yield {}   # 一定要定义生成器
	print('file end...')


with file_open('slef_ex.py') as f:
	print('file processing...')


""":return
file open...
file processing...
file end...
"""

# 总结:
# 第2种方法简化了第1种方法，代码集中