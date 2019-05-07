
PAGE_MODEL = r'''
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.base_page import Basepage
from selenium import webdriver
from selenium.webdriver.common.by import By
from common import mylog

log = mylog.Log().getlog()

class %(page_name)s(Basepage):

    def __init__(self,driver):
        self.driver = driver



if __name__ == "__main__":
    pass
'''


TEST_MODEL = r'''
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from selenium import webdriver
from common import HTMLTestReportCN
import unittest
from common import mylog
import os,time

log = mylog.Log().getlog()

class test_%(test_name)s(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_1(self):
        pass


if __name__=="__main__":

    filePath = os.path.dirname(os.path.dirname(__file__))+'/report/'+time.strftime("%%Y-%%m-%%d", time.localtime())+'_%(test_name)s.html'
    testsuit = unittest.TestSuite()
    testsuit.addTest(%(test_name)s('test_1'))
    fp = open(filePath,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='测试报告',
        #description='',
        tester="feng233"
        )
    runner.run(testsuit)
'''
