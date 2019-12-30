# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-30 00:06
@Desc    : 字典的子类，提供了可哈希对象的计数
@Docs    :
"""


from collections import Counter

userList = ['ericzhang', 'ericzhang1', 'ericzhang1']

userList1 = Counter(userList)
print(userList1)
""":return
Counter({'ericzhang1': 2, 'ericzhang': 1})
"""


# update.

userList1.update(['ericzhang3','ericzhang3'])
print(userList1)
""":return
Counter({'ericzhang1': 2, 'ericzhang3': 2, 'ericzhang': 1})
"""


# most_common: top, 排序. 使用数据结构 堆
print(userList1.most_common(2))


