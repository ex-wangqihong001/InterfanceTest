'''
@Project:Test_ecshop
@Time:2021/8/31 22:31
@Author:Xiaowang
'''
from random import randint


class A():
    def add(self,a,b):
        return a + b

class B(A):
    def sub(self,a,b):
        return a - b

# print(B().add(4,1))

class C():
    try:
        # open('aa.txt','r')
        aa = '异常测试'
        print(aa)
    except Exception as msg:
        print(msg)
    finally:
        print('不管如何，我都要执行！')

class D(object):
    def isnumber(self):
        self.number = randint(1,100)
        if self.number % 2 == 0:
            raise NameError('假装这里有个错误，下面一行的print就不会执行了')
            print('%d 是个偶数！' %self.number)
        else:
            print('%d 是个奇数！'% self.number)

if __name__ == '__main__':
    D().isnumber()