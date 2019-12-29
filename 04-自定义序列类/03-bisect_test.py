# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-29 09:13
@Desc    :            
@Docs    : 
"""

# bisect: 数组二分查找算法
# 1. 用来处理已排序的序列
# 2. 用来维持已排序的序列. 升序
# 3. 二分查找, 效率高

import bisect

seq_list = [n for n in range(20)]

print(seq_list)

print(bisect.insort_left(seq_list, 11))
print(seq_list)