# -*- encoding: utf-8 -*-
"""
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-12-30 12:52
@Desc    :            
@Docs    : 
"""


from collections import ChainMap


userDict1 = {'user1':'ericzhang1', 'user2':'ericzhang2'}
userDict2 = {'user2':'ericzhang2', 'user3':'ericzhang3'}

# 需要取出字典中数值，原始的方法只能循环
for user, name in userDict1.items():
	print(user, name)

for user, name in userDict2.items():
	print(user, name)


# 使用：from collections import ChainMap

from collections import ChainMap

new_dict = ChainMap(userDict1, userDict2)
print(new_dict)
""":return
ChainMap({'user1': 'ericzhang1', 'user2': 'ericzhang2'}, {'user2': 'ericzhang2', 'user3': 'ericzhang3'})
"""

new_dict.maps