
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.base_page import Basepage
from selenium import webdriver
from selenium.webdriver.common.by import By
from common import mylog

log = mylog.Log().getlog()

class Baidu(Basepage):

    def __init__(self,driver):
        self.driver = driver

    def get_start(self):
        self.driver.get("https://www.baidu.com/")
        log.info('访问主页')
        self.wait_element().presence(By.XPATH,"//input[@id='kw']")
        self.get_screenshot()
        self.send_key((By.XPATH,"//input[@id='kw']"),'baidu')
        self.sleep(10)
        self.click(By.XPATH,"//input[@id='su']")
        self.sleep(10)
        log.info('查找')
        self.get_screenshot()

if __name__ == "__main__":
    pass
