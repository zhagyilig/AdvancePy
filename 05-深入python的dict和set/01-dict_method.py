# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'


"""
dict常见的用法:
clean
copy
formkeys // 可迭代的对象转换成dict
get
items  // 返回k，v 一个tuple
setdefault
update
"""


my_dict = dict()

new_dict = {'name':'erichang', 'age':22}


# print(dir(new_dict))
""":return
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""


# new_dict.clear()
# print(new_dict)
""":return
{}
"""


my_list = ['ericzhang1', 'ericzhang2']
new_dict1 = my_dict.fromkeys(my_list, {'love':'python'})
print(new_dict1)

""":return
{'ericzhang1': {'love': 'python'}, 'ericzhang2': {'love': 'python'}}
"""

print(new_dict.get('name1', 1))


for k, v in new_dict.items():
	print(k, v)

""":return
name erichang
age 22
"""


new_dict.setdefault('name1', 'ericzhang3')
print(new_dict)


for k  in new_dict.keys():
	print(k)
for v in  new_dict.values():
	print(v)


print(new_dict, new_dict1)

new_dict.update(new_dict1)
print(new_dict)