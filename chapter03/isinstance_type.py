# -*- encoding: utf-8 -*-
'''
@Author  :   ericzhang 
@Version :   python3.6
@File    :   isinstance_type.py
@Time    :   2019/11/10 17:25:09
@Desc    :   建议使用 isinstance 查看类型,而不是type
@Docs    :            
'''


class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b, B))
print(isinstance(b, A))

print(type(b) == A)

"""
True
True
False
"""


"""
== 是判断值是不是相同
is 对象的 id 是不是相同
"""