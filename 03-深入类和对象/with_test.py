# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-28 17:28
@Desc    :            
@Docs    : 
"""


# 上下文管理器协议

class Sample:
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