# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'


def gen_func():
	""" 生成器函数: 函数只要有 yield 关键字. """
	yield 1
	yield 2

def func():
	""" 普通函数. """
	return 1


if __name__ == '__main__':
    gen = gen_func()
    # print(gen) # <generator object gen_func at 0x7f30a23aa048>
    for n in gen:
        print(n)

    print(func())

with open() as f:
	f.read()