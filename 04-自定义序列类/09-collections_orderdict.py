# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-30 00:17
@Desc    :  字典的子类，保存了他们被添加的顺序
@Docs    : 
"""


from collections import OrderedDict

# dict 在 py2 中无序的，但在 py3 后默认有序

user_dict = OrderedDict()

user_dict['a'] = 1
user_dict['b'] = 2
user_dict['c'] = 3

print(user_dict)
""":return
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
"""

user_dict.move_to_end('b') # 把 b 元素移动到之后
print(user_dict)
""":return
OrderedDict([('a', 1), ('c', 3), ('b', 2)])
"""

from collections import ChainMap