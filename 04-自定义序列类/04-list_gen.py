# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-29 10:25
@Desc    :            
@Docs    : 
"""

# 列表推导式
my_list = [n for n in range(10) if n%2 ==1 ]

print(my_list)
""":return
[1, 3, 5, 7, 9]
"""

# 生成器表达式
my_gen = (n for n in range(10))
print(type(my_gen))
print(my_gen)
""":return
<class 'generator'>
<generator object <genexpr> at 0x7fd109d000a0>
"""

new_list  = list(my_gen)
print(type(new_list))
print(new_list)
""":return
<class 'list'>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# 字典推导式
my_dict = {'name':'eric', 'age':'23'}
print(type(my_dict))
print(my_dict)
new_dict = {v:k for k,v in my_dict.items()}
print(type(new_dict))
print(new_dict)
""":return
<class 'dict'>
{'name': 'eric', 'age': '23'}
<class 'dict'>
{'eric': 'name', '23': 'age'}
"""


# 结合推导式

