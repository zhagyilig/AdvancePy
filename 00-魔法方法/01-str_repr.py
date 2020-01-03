# -*- encoding: utf-8 -*-
__author__ = 'ericzhang'

"""
str（）内置函数使用 __str__ 显示对象的字符串表示形式，而 repr（）内置函数使用 __repr__显示对象
"""

##
class Test:
    pass

print(str(Test()))
print(repr(Test()))
print(str(Test()) == repr(Test()))
""":return
<__main__.Test object at 0x7f6e8d4659b0>
<__main__.Test object at 0x7f6e8d4659b0>
True
"""


##
class Test1:
    def __str__(self):
        return "Test1.__str__"

print(str(Test1()))
print(repr(Test1()))
print(str(Test1()) == repr(Test1()))
""":return
Test1.__str__
<__main__.Test1 object at 0x7f6ed72559e8>
False
"""

##
class Test2:
    def __repr__(self):
        return "Test1.__str__"

print(str(Test2()))
print(repr(Test2()))
print(str(Test2()) == repr(Test2()))
""":return
Test1.__str__
Test1.__str__
True
"""


##
class Test3:
    def __repr__(self):
        return "Test3.__repr__"
    def __str__(self):
        return "Test3.__str__"


print(str(Test3()))
print(repr(Test3()))
print(str(Test3()) == repr(Test3()))
""":return
Test3.__str__
Test3.__repr__
False

"""

"""
通过上述例子的对比
1. 当仅定义 __repr__ 的时候， __repr__ == __str__, 但是仅定义 __str__ 的情况下，两者不相等
2. 显然当两者均定义的时候，会各自使用自己的方法
3. 两者的区别
_str_用于为最终用户创建输出，而 _repr_ 主要用于调试和开发。 _repr_ 的目标是明确无误，_str_ 是可读的
_repr_ 用于推断对象的"官方"字符串表示形式（包含有关对象的所有信息的表示, _str_ 用于推断对象的“非正式”字符串表示形式（对打印对象有用的表示形式
"""



##
import datetime
today = datetime.datetime.now()

print(str(today))
print(repr(today))

""":return
2020-01-03 10:37:35.101494
datetime.datetime(2020, 1, 3, 10, 37, 35, 101494)
"""
