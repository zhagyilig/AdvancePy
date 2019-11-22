# -*- encoding: utf-8 -*-
'''
@Author  :   ericzhang 
@Version :   python3.6
@File    :   attr_mro.py
@Time    :   2019/11/10 21:44:10
@Desc    :            
@Docs    :        
'''

# MRO 算法

# 深度优先

class A:
    name = 'eric1'
    # def __init__(self):
    #     self.name = 'eric2'

a = A()
print(a.name)

print(A.__mro__)  
# (<class '__main__.A'>, <class 'object'>)

