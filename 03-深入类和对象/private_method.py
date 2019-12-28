# -*- encoding: utf-8 -*-
'''
@Author  :   ericzhang 
@Version :   python3.6
@File    :   private_method.py
@Time    :   2019/11/10 22:33:46
@Desc    :   数据封装和私有属性       
@Docs    :            
'''

import os
import sys

from class_methid import Data

class User:
    def __init__(self, birthday):
        self.__birthday = birthday  # 私有属性 __ 私有属性只能在当前class访问

    def get_age(self):
        return 2019 - self.__birthday.year


if __name__ == '__main__':
    data_str = Data(1990, 1, 11)
    user = User(data_str)
    print(user._User__birthday)  # 访问私有属性, 格式:  _class__attr

    print(user.get_age())