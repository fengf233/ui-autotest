from basepage import mylog
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *
import time,os
import json
log = mylog.Log().getlog()

class Basepage():

    def __init__(self,driver):
        self.driver = driver

    #查找元素

    def find(self,*key):
        '''
        e.g.
            self.find(By.ID,"test")
        
        返回webelement对象,可以使用其所有方法,常用的有:
        - webelement.click()
        - webelement.clear()
        - webelement.send_keys(str)
        - webelement.submit()
        - webelement.size
        - webelement.text
        - webelement.get_attribute(name)
        - webelement.is_displayed()
        - webelement.is_selected()
        ....

        e.g.
            self.find(By.ID,"test").click()
        '''
        try:
            log.info("查找元素: %s" %key[1])
            return self.driver.find_element(*key)
        except Exception as e:
            log.error("没有找到元素: %s 异常为:\n %s" %(key[1],e))
            raise
        

    def finds(self,*key):
        '''
        e.g.
            self.finds(By.ID,"test")
        
        返回webelement对象列表,可以使用其所有方法
        '''
        try:
            log.info("查找元素: %s" %key[1])
            return self.driver.find_elements(*key)
        except Exception as e:
            log.error("没有找到元素: %s 异常为:\n %s" %(key[1],e))
            raise
    
    #界面等待

    def wait_element(self):
        '''
        显性等待
        -presence 等待元素出现在DOM,有则返回webelement对象 e.g. self.wait_element().presence(By.ID,"test")
        -visibility 等待元素显示在界面,有则返回webelement对象 e.g. self.wait_element().visibility(By.ID,"test")
        -invisibility 等待元素消失在界面 e.g. self.wait_element().invisibility(By.ID,"test")
        -alert 等待弹窗出现 e.g. self.wait_element().alert(timeout=10)
        -inalert 等待弹窗消失 e.g. self.wait_element().inalert(timeout=10)
        -custom 自定义 self.wait_element.custom().until(self.judge_element().title_is)
        '''
        return self.Wait_element(self.driver)

    class Wait_element():

        def __init__(self,driver):
            self.driver = driver

        def presence(self,*key,timeout=2,frequency=0.5):
            try:
                log.info("等待元素出现: %s" %key[1])
                return WebDriverWait(self.driver,timeout,poll_frequency=frequency).until(EC.presence_of_element_located(key))
            except TimeoutException:
                log.error("等待元素出现超时: %s" %key[1])
                raise

        def visibility(self,*key,timeout=2,frequency=0.5):
            try:
                log.info("等待元素显示: %s" %key[1])
                return WebDriverWait(self.driver,timeout,poll_frequency=frequency).until(EC.visibility_of_element_located(key))
            except TimeoutException:
                log.error("等待元素显示超时: %s" %key[1])
                raise

        def invisibility(self,*key,timeout=2,frequency=0.5):
            try:
                log.info("等待元素消失: %s" %key[1])
                return WebDriverWait(self.driver,timeout,poll_frequency=frequency).until(EC.invisibility_of_element_located(key))
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
            #自定义 self.wait_element.custom().until(self.judge_element().title_is)
            return WebDriverWait(self.driver,timeout,poll_frequency=frequency)

    def sleep(self,seconds):
        log.info("界面等待%s秒"%seconds)
        time.sleep(seconds)

    def implicitly_wait(self,seconds=10):
        self.driver.implicitly_wait(seconds)
        log.info("全局等待时间为%s秒"%seconds)

    #界面操作

    def window_size(self,*size):
        if size:
            self.driver.set_window_size(*size)
        else:
            self.driver.maximize_window()

    def get_url(self):
        log.info("当前页面的url: %s" % self.driver.current_url)
        return self.driver.current_url

    def get_title(self):
        log.info("当前页面的title: %s" % self.driver.title)
        return self.driver.title

    def click(self,*key):
        '''
        e.g. self.click(By.ID,"test")
        '''
        try:
            self.find(*key).click()
            log.info('点击元素：%s' %key[1])
        except:
            log.error("无法点击元素")
            raise

    def send_key(self,key,text):
        '''
        e.g. self.send_key((By.ID,"test"),"11111")
        '''
        log.info('清空输入框内容')
        self.find(*key).clear()
        log.info('输入内容: %s' %text)
        try:
            self.find(*key).send_keys(text)
        except:
            log.error("输入内容失败")
            raise
    
    def clear(self,*key):
        '''
        e.g. self.clear(By.ID,"test")
        '''
        log.info('清除元素内容：%s' %key[1])
        try:
            self.find(*key).clear()
        except:
            log.error("无法清除元素内容")
            raise
    
    def switch_to_window(self,handle):
        self.driver.switch_to_window(handle)
        log.info('切换到[%s]窗口'%self.get_title())

    def switch_to_frame(self,*key):
        '''
        切换框架,直接输入iframe的name或id属性，或者传入定位的元素

        e.g.
        self.switch_to_frame("if")
        self.switch_to_frame(By.ID,"if")
        '''
        if len(key) == 2:
            xf = self.find(*key)
            self.driver.switch_to_frame(xf)
            log.info("切换到[%s]frame表单"%key[1])
            return ''
        self.driver.switch_to_frame(key)
        log.info("切换到[%s]frame表单"%key)

    def quit(self):
        self.driver.quit()
        log.info("关闭浏览器")
    
    def close(self):
        self.driver.close()
        log.info("关闭窗口")

    def forward(self):
        self.driver.forward()
        log.info("前进一个界面")
    
    def refresh(self):
        self.driver.refresh()
        log.info("刷新界面")

    def back(self):
        self.driver.back()
        log.info("前进一个界面")

    def get_screenshot(self):
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__))+ '/report/'+type(self).__name__+'/screenshot/')
        if os.path.exists(file_path) and os.path.isdir(file_path):
            pass
        else:
            os.makedirs(file_path)
        img_name = file_path + time.strftime("%Y-%m-%d-%H%M", time.localtime()) + '.png'
        try:
            self.driver.get_screenshot_as_file(img_name)
            log.info("截图保存至:%s"%img_name)
        except Exception as e:
            log.error("截图失败:%s"%e)

    #检查元素的可用性

    def judge_element(self):
        '''
        e.g. self.judge_element().presence_of_element_located((By.ID,"test"))
        '''
        return EC

    def title_is(self,title):
        '''
        e.g. self.title_is("test")
        返回true或false
        '''
        return EC.title_is(title)(self.driver)

    def title_contains(self,title):
        '''
        title是否包含字段
        e.g. self.title_contains("test")
        返回true或false
        '''
        return EC.title_contains(title)(self.driver)

    def element_presence(self,*key):
        '''
        e.g. self.element_presence(By.ID,"test")
        元素存在则返回webelement对象或false
        '''
        #元素存在则返回webelement对象
        return EC.presence_of_element_located(key)(self.driver)

    def element_visibility(self,*key):
        '''
        e.g. self.element_visibility(By.ID,"test")
        元素显示则返回webelement对象或false
        '''
        #元素显示则返回webelement对象
        return EC.visibility_of_element_located(key)(self.driver)

    def url_contains(self,url):
        '''
        判断给定url是否包含在当前url中
        '''
        return EC.url_contains(url)(self.driver)

    def alert_is_present(self):
        '''
        e.g. self.alert_is_present()
        弹出框显示则返回alert对象或false
        '''
        return EC.alert_is_present()(self.driver)
    
    def switch_alert(self):
        return self.driver.switch_to_alert()

    def click_alert(self):
        try:
            self.alert_is_present().accept()
        except NoAlertPresentException:
            raise

    def dismiss_alert(self):
        try:
            self.alert_is_present().dismiss()
        except NoAlertPresentException:
            raise

    #js脚本操作

    def execute_js(self,js,*key):
        '''
        e.g. self.execute_js("window.scrollTo(0,0))
        '''
        if key:
            log.info("对元素执行js脚本:%s"%js)
            return self.driver.execute_script(js,self.find(*key))
        else:
            log.info("执行js脚本:%s"%js)
            return self.driver.execute_script(js)

    def execute_async_js(self,js,*key):
        #异步执行
        if key:
            log.info("对元素执行js脚本:%s"%js)
            return self.driver.execute_async_script(js,self.find(*key))
        else:
            log.info("执行js脚本:%s"%js)
            return self.driver.execute_async_script(js)

    #cookies操作
    def get_cookies(self):
        return self.driver.get_cookies()

    def add_cookie(self,cookie_dict):
        self.driver.add_cookie(cookie_dict)
        
    def save_cookies(self):
        '''
        保存cookies为json文件
        '''
        cookies = self.driver.get_cookies()
        cookies_path = os.path.join(os.path.dirname(os.path.dirname(__file__))+ '/report/'+type(self).__name__+'/cookies/')
        if os.path.exists(cookies_path):
            pass
        else:
            os.makedirs(cookies_path)
        cookies_file = cookies_path +'cookies.json'
        with open(cookies_file,'w') as f:
            json.dump(cookies,f)
        log.info('cookies保存在:%s'%cookies_path)
        return cookies_file

    def add_cookies(self,cookies_file=''):
        '''
        从cookies.json文件添加所有cookies
        '''
        if not cookies_file:
            cookies_file = os.path.join(os.path.dirname(os.path.dirname(__file__))+ '/report/'+type(self).__name__+'/cookies/') +'cookies.json'
        with open(cookies_file,'r') as f :
            cookies = json.load(f)
            # self.driver.delete_all_cookies()
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        log.info('cookies加载成功:%s'%cookies_file)


    #行为链,直接返回action api,自己定义更方便

    def action(self):
        '''
        行为链操作，以perform()提交操作
        e.g.
        action = self.action()
        action.move_to_element(element).click(element).perform()
        '''
        return ActionChains(self.driver)
