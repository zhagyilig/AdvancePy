# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'


class Commpany:
	def __init__(self, user_list):
		self.user_list = user_list

	def __getitem__(self, item):
		return self.user_list[item]

	def __len__(self):
		return len(self.user_list)

if __name__ == '__main__':
    company = Commpany(['ericzhang1', 'ericzhang2', 'ericzhang3' ])
    print(len(company))
    for n in company:
	    print(n)

