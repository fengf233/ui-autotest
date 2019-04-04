from basepage import mylog
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time,os
log = mylog.Log().getlog()

class Basepage():

    def __init__(self,driver):
        self.driver = driver

    #查找元素

    def find(self,*key):
        try:
            return self.driver.find_element(*key)
        except NoSuchElementException:
            log.error("没有找到元素: %s" %key[1])
            raise
        except TimeoutException:
            log.error("查找元素超时: %s" %key[1])
            raise

    def finds(self,*key):
        try:
            return self.driver.find_elements(*key)
        except NoSuchElementException:
            log.error("没有找到元素: %s" %key[1])
            raise
        except TimeoutException:
            log.error("查找元素超时: %s" %key[1])
            raise

    def wait_element(self):
        return self.Wait_element(self.driver)

    class Wait_element():

        def __init__(self,driver):
            self.driver = driver

        def presence(self,*key,timeout=2,frequency=0.5):
            try:
                log.info("等待元素出现: %s" %key[1])
                return WebDriverWait(self.driver,timeout,poll_frequency=frequency).until(EC.presence_of_element_located((*key)))
            except TimeoutException:
                log.error("等待元素出现超时: %s" %key[1])
                raise

        def visibility(self,*key,timeout=2,frequency=0.5):
            try:
                log.info("等待元素显示: %s" %key[1])
                return WebDriverWait(self.driver,timeout,poll_frequency=frequency).until(EC.visibility_of_element_located((*key)))
            except TimeoutException:
                log.error("等待元素显示超时: %s" %key[1])
                raise

        def invisibility(self,*key,timeout=2,frequency=0.5):
            try:
                log.info("等待元素消失: %s" %key[1])
                return WebDriverWait(self.driver,timeout,poll_frequency=frequency).until(EC.invisibility_of_element_located((*key)))
            except TimeoutException:
                log.error("等待元素消失超时: %s" %key[1])
                raise

        def alert(self,timeout=2,frequency=0.5):
            try:
                log.info("等待弹窗出现")
                return WebDriverWait(self.driver,timeout,poll_frequency=frequency).until(EC.alert_is_present())
            except TimeoutException:
                log.error("等待弹窗出现超时")
                raise

        def inalert(self,timeout=2,frequency=0.5):
            try:
                log.info("等待弹窗消失")
                return WebDriverWait(self.driver,timeout,poll_frequency=frequency).until_not(EC.alert_is_present())
            except TimeoutException:
                log.error("等待弹窗消失超时")
                raise

        def custom(self,timeout=2,frequency=0.5):
            return WebDriverWait(self.driver,timeout,poll_frequency=frequency)
            
    def wait(self,seconds):
        log.info("界面等待%s秒"%seconds)
        time.sleep(seconds)

    def implicitly_wait(self,seconds=10):
        self.driver.implicitly_wait(seconds)
        log.info("全局等待时间为%s秒"%seconds)

    #界面操作

    def get_url(self):
        log.info("当前页面的url: %s" % self.driver.title)
        return self.driver.current_url

    def get_title(self):
        log.info("当前页面的title: %s" % self.driver.title)
        return self.driver.title

    def quit(self):
        self.driver.quit()
        log.info("关闭浏览器")
    
    def close(self):
        self.driver.close()
        log.info("关闭窗口")

    def forward(self):
        self.driver.forward()
        log.info("前进一个界面")

    def back(self):
        self.driver.back()
        log.info("前进一个界面")

    def get_screenshot(self):
        file_path = './report/'+type(self).__name__+'/screenshot/'
        if os.path.exists(file_path) and os.path.isdir(file_path):
            pass
        else:
            os.makedirs(file_path)
        img_name = file_path + time.strftime("%Y-%m-%d-%H%M", time.localtime()) + '.png'
        try:
            self.driver.get_screenshot_as_file(img_name)
            log.info("截图保存为:%s"%file_path)
        except Exception as e:
            log.error("截图失败:%s"%e)

    #检查元素的可用性

    def judge_element(self):
        return self.Judge_element(self.driver)

    class Judge_element():


        def __init__(self,driver):
            self.driver = driver

        def 

    