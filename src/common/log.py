import logging
from config import globalparameter as GL
import time
'''
配置日志文件，输出INFO级别以上的日志
'''

class log(object):
    def __init__(self):
        self.logname = time.strftime('%Y%m%d%H%S', time.localtime())

    def setMSG(self, level, msg):

        logger = logging.getLogger()
        # 定义Handler输出到文件和控制台
        fh = logging.FileHandler(GL.log_name, 'a', encoding='utf-8')
        ch = logging.StreamHandler()
        # 定义日志输出格式
        formater = logging.Formatter("%(asctime)s %(filename)s文件 %(funcName)s函数 %(lineno)d行 %(levelname)s : %(message)s")
        fh.setFormatter(formater)
        ch.setFormatter(formater)
        # 添加Handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 添加日志信息，输出INFO级别的信息
        logger.setLevel(logging.INFO)
        if level == 'debug':
            logger.debug(msg)
        elif level == 'info':
            logger.info(msg)
        elif level == 'warning':
            logger.warning(msg)
        elif level == 'error':
            logger.error(msg)

        # 移除句柄，否则日志会重复输出
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()

    def debug(self, msg):
        self.setMSG('debug', msg)

    def info(self, msg):
        self.setMSG('info', msg)

    def warning(self, msg):
        self.setMSG('warning', msg)

    def error(self, msg):
        self.setMSG('error', msg)

if __name__  == "__main__":
    uer = log()
    a = uer.setMSG("warning", "测试日志模块")