# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'


# set 和 frozenset: 无序集合、去重
# frozenset 定义之后不能更改，可以用来 dict 的key
# set的时间复杂读 O(1)

## 初始化
s1 = set('abbbcc')  # iterable

s2 = frozenset('abbcccceee')

print(s1, s2)
""":return
{'a', 'c', 'b'} 
frozenset({'e', 'a', 'c', 'b'})
"""