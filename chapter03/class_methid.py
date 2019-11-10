# -*- encoding: utf-8 -*-
'''
@Author  :   ericzhang 
@Version :   python3.6
@File    :   class_methid.py
@Time    :   2019/11/10 21:59:40
@Desc    :   类方法、静态方法、实例方法       
@Docs    :            
'''


class Data:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法
    def tomorrow(self):
        self.day += 1

    # 静态方法
    @staticmethod
    def data_static_parse(data_str):
        year, month, day = data_str.split('-')
        return Data(year, month, day)

    # 类方法
    @classmethod
    def data_class_parsr(cls, data_str):
        year, month, day = data_str.split('-')
        return cls(year, month, day)

    def __str__(self):
        return '{}/{}/{}'.format(self.year, self.month, self.day)


if __name__ == '__main__':
    new_day = Data(2019, 11, 10)
    print(new_day)

    # 在外面解析合适的格式再传入类中
    # 2019-11-10
    data_str = '2019-11-10'
    year, month, day = data_str.split('-')
    print(year, month, day)
    new_day = Data(year, month, day)
    print(new_day)

    # 使用staticmothod完成初始化
    new_day = Data.data_static_parse(data_str)
    print(new_day)

    # 使用classmothod完成初始化
    new_day = Data.data_class_parsr(data_str)
    print(new_day)