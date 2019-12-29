# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-29 23:02
@Desc    :            
@Docs    : 
"""


from collections import defaultdict


my_dict = {}
my_list = ['ericzhang1', 'ericzhang2', 'ericzhang1']

# 1.
for n in my_list:
	if n not in my_dict:
		my_dict[n] = 1
	else:
		my_dict[n] += 1

print(my_dict)

""":return
{'ericzhang1': 2, 'ericzhang2': 1}
"""

# 2. setdefault
my_dict = {}
for n in my_list:
	my_dict.setdefault(n, 0)
	my_dict[n] += 1

print(my_dict)

""":return
{'ericzhang1': 2, 'ericzhang2': 1}
"""


# 3. defaultdict
default_dict = defaultdict(int)
for n in my_list:
	default_dict[n] += 1
print(default_dict)

""":return
defaultdict(<class 'int'>, {'ericzhang1': 2, 'ericzhang2': 1})
"""
