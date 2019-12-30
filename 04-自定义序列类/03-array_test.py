# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-29 10:04
@Desc    :            
@Docs    : 
"""


# array deque
# array 和 list 主要的区别: array只能存放指定的数据类型
# doc: https://docs.python.org/zh-cn/3.6/library/array.html?highlight=array#module-array

import array


my_array = array.array('i')

my_array.append(1)
my_array.append(1)
my_array.append(1)
my_array.append(1)

print(my_array)

