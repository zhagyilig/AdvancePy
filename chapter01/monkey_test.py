# coding=utf-8

'''
@Author  : ericzhang
@Version : python3.7
@Date    : 2019-11-10 10:17
@Soft    : PyCharm
@Desc    :
@Docs    :
'''


class Student(object):
    def say(self):
        return 'i am study'


student = Student()


def teacher():
    return 'i am teacher'


student.say = teacher()

print(student.say)

"""
i am teacher
"""
