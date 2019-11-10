# coding=utf-8

'''
@Author  : ericzhang
@Version : python3.7
@Date    : 2019-11-10 10:24
@Soft    : PyCharm
@Desc    : 鸭子类型: 所有的类都实现了一个方法(方法名字一样)
@Docs    :
'''

## 1
class Cat(object):
    def say(self):
        print('i am a cat')

class Dog(object):
    def say(self):
        print('i am a dog')

class Duck(object):
    def say(self):
        print('i am a duck')

animal_list = [Cat, Dog, Duck]

# 使用了 python class 多态的特性
for animal in animal_list:
    animal().say()
    """
    i am a cat
    i am a dog
    i am a duck
    """

class Company(object):
    def __init__(self, employes_list):
        self.employes_list = employes_list

    def __getitem__(self, item):
        return self.employes_list[item]

employes_list = ['eric11', 'eric12']

com = Company(employes_list)
for n in com:
    print(n)
# 2

a = ['eric1', 'eric2']
b = ['eric7', 'eric8']
name_tuple = ('eric3', 'eric4')

name_set=set()
name_set.add('eric5')
name_set.add('eric6')


a.extend(name_set)
print(a)  # ['eric1', 'eric2', 'eric6', 'eric5']


a.extend(com)
print(a) # ['eric1', 'eric2', 'eric6', 'eric5', 'eric11', 'eric12']