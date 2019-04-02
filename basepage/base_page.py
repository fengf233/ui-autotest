from basepage import mylog
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
log = mylog.Log().getlog()

class Basepage():

    def __init__(self,driver):
        self.driver = driver

    def find(self,*key):
        return self.driver.find_element(*key)

    def finds(self,*key):
        return self.driver.find_elements(*key)

    def wait_element(self,*key,timeout=2):
        #
        def presence():
            WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((*key)))
        def visibility():
            WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((*key)))
        def invisibility():
            WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located((*key)))
        def alert():
            WebDriverWait(self.driver,timeout).until(EC.alert_is_present((*key)))
        #自己选择显示等待条件
        def until(*k):
            WebDriverWait(self.driver,timeout).until(*k)
