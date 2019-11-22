# -*- encoding: utf-8 -*-
'''
@Author  :   ericzhang
@Version :   python3.6
@File    :   slef_ex.py
@Time    :   2019/11/11 23:53:06
@Desc    :   pyhon的自省机制：通过一定的机制查询到对象的内部结构
@Docs    :
'''


class Person:
    """person."""
    name = 'eric'


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name
        self.county = 'hubei'
        self.teacher = 'eric'


if __name__ == '__main__':
    user = Student('wuhan')
    print(user.__dict__)
    # {'school_name': 'wuhan', 'county': 'hubei', 'teacher': 'eric'}
    print(user.__dict__.get('school_name')) # wuhan
    print(dir(user.__dict__))   
    print(user.name)  # eric  Student继承Person. user.name 向上传递
    print(Person.__doc__) # person.