# coding=utf-8

'''
@Author  : ericzhang
@Version : python3.7
@Date    : 2018-08-10 09:23
@Soft    : PyCharm
@Desc    :            
@Docs    : 
'''


a=1
b="abc"
print(type(1))
print(type(int))
print(type(b))
print(type(str))

# type -> int   -> 1
# type -> class -> obj

class Student:  # 默认继承object
    pass

stu = Student()
print(type(stu))
print(type(Student))
print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
print(type.__bases__)
print(object.__bases__)
print(type(object))



