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

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.employee) > 2:
            raise StopIteration
        else:
            self.employee += 1
            return self.employee

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        return ','.join(self.employee)

    def __repr__(self):
        return '-'.join(self.employee)


company = Company(['pudong', 'jiading', 'changning'])

## 获取list
print('------')
em = company.employee
for item in em:
    print(item)

"""
pudong
jiading
changning
"""

## 获取list，使用魔法函数 __getitem__
print('------')
for em in company:
    print(em)
"""
pudong
jiading
changning
"""


## 切片

company1 = company[:2]
print('------')
for em in company1:
    print(em)


## __len__
print('------')
print(len(company))

## __str__
print('------')
print(company)


"""
总结：
1、python中所有的迭代环境都会先尝试__iter__方法，再尝试__getitem__，只有在对象不支持迭代协议时，才会尝试索引
2、把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
"""