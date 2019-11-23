# -*- encoding: utf-8 -*-
'''
@Author  :  ericzhang
@Version :  python3
@Date    :  2019-11-23 20:58
@Desc    :  条件变量, 用于复杂的线程间同步
@Docs    : 
'''

import time
import threading

class Xiaomi(threading.Thread):
    def __init__(self, cond):
        # threading.Thread.__init__(self, name='小爱')
        super(Xiaomi, self).__init__(name='小爱')
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            time.sleep(1)
            print("{} : 在 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            time.sleep(1)
            print("{} : 好啊 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            time.sleep(1)
            print("{} : 君住长江尾 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            time.sleep(1)
            print("{} : 共饮长江水 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            time.sleep(1)
            print("{} : 此恨何时已 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            time.sleep(1)
            print("{} : 定不负相思意 ".format(self.name))
            self.cond.notify()

class Tianmao(threading.Thread):
    def __init__(self, cond):
        super(Tianmao, self).__init__(name='天猫精灵')
        self.cond = cond

    def run(self):
        with self.cond:
            print("{} : 小爱同学".format(self.name))
            self.cond.notify()
            self.cond.wait()
            time.sleep(1)


            print("{} : 我们来对古诗吧 ".format(self.name))
            self.cond.notify()
            self.cond.wait()
            time.sleep(1)

            print("{} : 我住长江头 ".format(self.name))
            self.cond.notify()
            self.cond.wait()
            time.sleep(1)

            print("{} : 日日思君不见君 ".format(self.name))
            self.cond.notify()
            self.cond.wait()
            time.sleep(1)

            print("{} : 此水几时休 ".format(self.name))
            self.cond.notify()
            self.cond.wait()
            time.sleep(1)

            print("{} : 只愿君心似我心 ".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    cond = threading.Condition()  # 实例化条件
    xiaomo = Xiaomi(cond)
    tianmao = Tianmao(cond)

    #启动顺序很重要
    #在调用with cond之后才能调用wait或者notify方法
    #condition有两层锁， 一把底层锁会在线程调用了wait方法的时候释放， 上面的 \
    #锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等到notify方法的唤醒
    xiaomo.start()
    tianmao.start()