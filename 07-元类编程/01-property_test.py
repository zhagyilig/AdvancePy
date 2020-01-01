# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'

# python 的实例化过程
# property 动态属性

from datetime import date, datetime


class User:
	def __init__(self, user, birthday):
		self.user = user
		self.birthday = birthday
		self._age = 0

	def get_age(self):
		return datetime.now().year - self.birthday.year

	@property  # 动态属性
	def age(self):
		return datetime.now().year - self.birthday.year

	@age.setter
	def age(self, value):
		self._age = value

if __name__ == '__main__':
    user = User('ericzhnag', date(year=1994, month=12, day=12))
    print(user.get_age())
    print(user.age)

    user.age = 25
    print(user._age)