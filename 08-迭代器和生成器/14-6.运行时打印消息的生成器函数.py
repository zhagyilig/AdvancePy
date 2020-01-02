# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'


def gen_AB():
	print('start')
	yield 'A'
	print('continue')
	yield 'B'
	print('end')

for c in gen_AB():
	# for 机制会捕获异常，因此循环终止时没有报错。
	print('--> ', c)

""":return
start
-->  A
continue
-->  B
end
"""