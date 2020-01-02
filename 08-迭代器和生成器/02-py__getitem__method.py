# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'


# Python的魔法方法__getitem__ 可以让对象实现迭代功能，这样就可以使用for...in... 来迭代该对象了

# 在用 for..in.. 迭代对象时，如果对象没有实现 __iter__ __next__ 迭代器协议，Python的解释器就会去寻找__getitem__ 来迭代对象，如果连__getitem__ 都没有定义，这解释器就会报对象不是迭代器的错误： TypeError: 'Animal' object is not iterable


class Animal:
    def __init__(self, animal_list):
        self.animals_name = animal_list

animals = Animal(["dog","cat","fish"])
# for animal in animals:
#     print(animal)  # TypeError: 'Animal' object is not iterable


# 而实现这个方法后，就可以正常迭代对象了

from collections.abc import Iterator

class Animal:
    def __init__(self, animal_list):
        self.animals_name = animal_list

    def __getitem__(self, index):
        print(index)
        return self.animals_name[index]


class Animalator(Iterator):
    """ Iterator继承了 __iter__ """
    def __next__(self):
        return self

animals = Animal(["dog","cat","fish"])
for animal in animals:
	print(animal)
""":return
dog
cat
fish
"""