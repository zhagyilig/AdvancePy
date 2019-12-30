# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-29 23:24
@Desc    :  类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop)
@Docs    :  https://docs.python.org/zh-cn/3.6/library/collections.html?highlight=collections#module-collections
"""

# deque 和 list 最大的区别就是 deque 是线程安全的

from queue import Queue
""" Queue 就是使用 from collections import deque
# Initialize the queue representation
def _init(self, maxsize):
    self.queue = deque()
"""

from collections import deque  # 双端队列


userList = ['ericzhang1', 'ericzhagn2']

username = userList.pop() #  pop弹出最后一个值, 不能对第一个值操作. 而 deque 能实现.

print(username, userList)
""":return
ericzhagn2 ['ericzhang1']
"""

# deque.
userList = deque(['ericzhang1', 'ericzhang2'])  # deque(iterable)
print(userList)

userList.appendleft('ericzhang3')
print(userList)
""":return
deque(['ericzhang1', 'ericzhang2'])
"""

""":return
deque(['ericzhang3', 'ericzhang1', 'ericzhang2'])
"""



