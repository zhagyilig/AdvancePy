# coding=utf-8

'''
@Author  : ericzhang
@Version : python3.7
@Date    : 2019-11-10 10:24
@Soft    : PyCharm
@Desc    : python 魔法函数
@Docs    : 
'''


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(['pudong', 'jiading', 'changning'])

## 获取list
em = company.employee
for item in em:
    print(item)

"""
pudong
jiading
changning
"""


## 获取list，使用魔法函数 __getitem__
for em in company:
    print(em)
"""
pudong
jiading
changning
"""


## 切片

company1 = company[:2]
print('----------')
for em in company1:
    print(em)


##
print('--------')
print(len(company))