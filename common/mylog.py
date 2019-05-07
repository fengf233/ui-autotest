#coding:utf-8
import logging
import time,os
'''
    使用方法：
    import mylog
    log = mylog.Log().getlog()
    log.debug("###")
'''
class Log():

    def __init__(self,logger="mylog"):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.log_time = "\\"+time.strftime("%Y-%m-%d_%H_%M", time.localtime())+".log"
        # 在进程路径创建log文件夹
        # self.log_path = os.path.join(os.getcwd() + "\\log")
        # 固定在mylog上一级创建
        self.log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + "\\log")
        if os.path.exists(self.log_path) and os.path.isdir(self.log_path):
            pass
        else:
            os.makedirs(self.log_path)
        self.log_name = os.path.join(self.log_path + self.log_time)

        #因为多出调用logger会生成多个handlers,所以每次调用清空handler
        self.logger.handlers = [] 
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        formatter = logging.Formatter('[%(levelname)s][%(asctime)s] [%(filename)s]->[%(funcName)s] line:%(lineno)d ---> %(message)s')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        
        fh.close()


    def getlog(self):
        return self.logger

if __name__ == "__main__":
    log = Log().getlog()
    log.debug("hello")
    