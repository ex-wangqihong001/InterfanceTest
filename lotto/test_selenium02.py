'''
@Project:Test_ecshop
@Time:2021/8/31 22:33
@Author:Xiaowang
'''
from lotto.case.test_selenium01 import A,D

class B1():
    result = A().add(4,5)
    print(result)

# 拼接当前地址，然后生成一个路径地址
import time
import os
now = time.strftime('%Y-%m-%d %H-%M-%S')
getdir = os.getcwd()
new = os.path.join(getdir,now)
print(now)
print(getdir)
print(new + '_result.html')

# import random
# print(random.randint(0,1000))



