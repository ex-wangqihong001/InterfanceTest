'''
@Project:Test_ecshop
@Time:2021/8/28 10:01
@Author:Xiaowang
'''

# 彩票开奖结果查询---待优化成弹框输入并且下拉栏选择双色球还是大乐透。还要选择日期
from pprint import pprint
import requests
import unittest
import logging
class  Test_lottoSearch(unittest.TestCase):
    # 定义成类属性
    @classmethod
    def setUpClass(cls):
        cls.url = 'http://apis.juhe.cn//lottery/bonus'
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test01(self):
        '''输入全部参数查询成功'''
        # lottery_id中dlt表示大乐透，ssq表示双色球

        params = {
            'key':'098da4754ea96454b65b83464f342ebe',
            'lottery_id':'dlt',
            'lottery_res':'01,07,21,30,35@08,11',
            'lottery_no':'21089'
        }

        r = requests.get(url=self.url,params=params)
        # print(r.request.method)
        # print(r.headers)
        # print(r.text)
        # p = "地址为：{.url}".format(r)
        # print(p)
        # print(resopnes.status_code)
        # pprint(resopnes.json())
        # print(("case:查询成功\n".format(r)))
        # print(("请求地址：{.url}".format(r)))
        # print(("c请求方式:{.request.method}".format(r)))
        # print(("响应头：{.headers}".format(r)))
        # print(("响应正文：{.text}".format(r)))

        status = r.json()['error_code']
        reason = r.json()['reason']
        # print(reason)
        self.assertEqual(status,0)
        logging.info("case:{}查询成功\n请求地址：{.url}\t请求方式:{.request.method}\n响应头：{.headers}\n响应正文：{.text}\n".format(reason,r,r,r,r))

    def test_02(self):
        '''key输入为空'''
        params = {
            'key':'',
            'lottery_id':'dlt',
            'lottery_res':'01,07,21,30,35@08,11',
            'lottery_no':'21089'
        }
        r = requests.get(url=self.url,params=params)
        status = r.json()['error_code']
        reason = r.json()['reason']
        self.assertEqual(status,10001,"错误的请求key")
        logging.info("case:{}\n请求地址：{.url}\t请求方式：{.request.method}\n响应头：{.headers}\n响应正文：{.text}\n".format(reason,r,r,r,r))

    def test_03(self):
        '''key值不正确'''
        params = {
            'key':'wwwww11232312321',
            'lottery_id':'dlt',
            'lottery_res':'01,07,21,30,35@08,11',
            'lottery_no':'21089'
        }

        r = requests.get(url=self.url,params=params)
        status = r.json()['error_code']
        reason = r.json()['reason']
        self.assertEqual(10001,status)

        # 先定义好格式（输入日志名称，输入等级，写入方式，写入的格式），再输出内容
        # logging.basicConfig(filename=r'D:\接口自动化测试\lotto\result\test.log',level=logging.INFO,filemode='w',format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # logging.basicConfig(level=logging.INFO,#控制台打印的日志级别
        #             filename='new.log',
        #             filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
        #             #a是追加模式，默认如果不写的话，就是追加模式
        #             format=
        #             '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        #             #日志格式
        #             )
        logging.info('case:11{}\n请求地址：{.url}\t请求方式：{.request.method}\n响应头：{.headers}\n响应正文：{.text}\n'.format(reason,r,r,r,r))
if __name__ == '__main__':
    unittest.main(verbosity=2)


