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

    def wait_element(self,*key,time=2):
        def presence():
            WebDriverWait(self.driver,time).until(EC.presence_of_element_located((*key)))
        def visibility():
            WebDriverWait(self.driver,time).until(EC.presence_of_element_located((*key)))