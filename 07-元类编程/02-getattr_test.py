# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'


# __getattr__, __getattribute__
# __getattr__ 就是在查找不到属性的时候调用
# __getattrbute__ 就是在查找属性之前调用，不管属性是否存在


from datetime import date

##
# class User:
# 	def __init__(self, name, birthday, info):
# 		self.name = name
# 		self.birthday = birthday
# 		self.info = info
#
# 	def __getattr__(self, item):
# 		return 'nnnn'
#
#
#
# if __name__ == '__main__':
#     user = User('ericzhang', '1994', info={'comm':'mt'})
#     print(user.ll)
    # nnnn

##
class User:
	def __init__(self, name, birthday, info):
		self.name = name
		self.birthday = birthday
		self.info = info

	def __getattr__(self, item):
		print(1111111, item)
		return self.info[item]


if __name__ == '__main__':
    user = User('ericzhang', '1994', info={'comm':'mt'})
    print(user.comm) # mt


##
# class User:
# 	def __init__(self, name, birthday,info):
# 		self.name = name
# 		self.birthday = birthday
#
# 	def __getattribute__(self, item):
# 		return '111'
#
#
# if __name__ == '__main__':
#     user = User('ericzhang', '1994',info={'comm':'mt'})
#     print(user.age['comm'])
