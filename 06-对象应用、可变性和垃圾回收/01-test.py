# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'


# is  ==
# is 是判断 id (内存地址) 是不是一样的
# == 是调用  __eq__ 魔法行数

my_list = [1,2,3]
my_list1 = [1,2,3]


print(id(my_list), id(my_list1))
print(my_list is my_list1)
print(my_list == my_list1)

""":return
139878848448392 139878848448968
False
True 
"""
