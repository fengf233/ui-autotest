
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from selenium import webdriver
from common import HTMLTestReportCN
import unittest
from common import mylog
import os,time
from page import baidu

log = mylog.Log().getlog()

class test_Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # print(logging.handlers)
        print("start")

    def tearDown(self):
        self.driver.quit()
        # print(logging.handlers)
        print("end")
    
    def screenshot(self,a):
        return a.get_screenshot()

    def test_1(self):
        log.info('----------开始测试1')
        a = baidu.Baidu(self.driver)
        self.screenshot(a)
        print("111111111")
        a.get_start()
        print("1111111111")

    def test_2(self):
        log.info('----------开始测试2')
        a = baidu.Baidu(self.driver)
        self.screenshot(a)
        print("222222222")
        a.get_start()
        print("22222222222")


if __name__=="__main__":

    filePath = os.path.dirname(os.path.dirname(__file__))+'/report/'+time.strftime("%Y-%m-%d", time.localtime())+'Baidu.html'
    testsuit = unittest.TestSuite()
    testsuit.addTest(test_Baidu('test_1'))
    testsuit.addTest(test_Baidu('test_2'))
    fp = open(filePath,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='测试报告',
        #description='',
        tester="feng233"
        )
    runner.run(testsuit)
