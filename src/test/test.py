#encoding=utf-8
#python version 3.4

'''
Created on 2015年10月10日

@author: shawn
'''
import unittest
##eclipse里不需要带src 转换到pycharm 需要做两件事 1.mark project as root  2.import 时候从顶层文件写起
from src.util import cookieUtil

from scalers import storePosts
from util import cookieUtil

#此测试用例可以执行。
class Test(unittest.TestCase):
    
    def setUp(self):
        print('test unitest  setup')

    def tearDown(self):
        print('test unitest  teardown')
        
    #def testCookieToDict(self):
    #   storePosts.convertCookieStrToDict();

    def testCookieToDict(self):
        print('testCookieToDict')
        self.assertEqual('4865368',cookieUtil.convertCookieStrToDict().get('o_cookie'),'cookieConvertToDictFailed')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()