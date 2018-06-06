from config import globalpara as gl
import logging

class Log:
    def __init__(self):
        self.logname = 'my.log'
    def setMSG(self,level,msg):
        logger = logging.getLogger()
        #定义handler输出到文件和控制台
        fh = logging.FileHandler(gl.log_path)
        ch = logging.StreamHandler()
        #定义日志输出格式
        formater = logging.Formatter("%(asctime)s %(levelname)s '%(message)s' ")
        fh.setFormatter(formater)
        ch.setFormatter(formater)
        #添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        #添加日志信息，输出INFO级别信息
        logger.setLevel(logging.INFO)
        if level == 'debug':
            logger.debug(msg)
        elif level == 'info':
            logger.info(msg)
        elif level == 'warning':
            logger.warning(msg)
        elif level == 'error':
            logger.error(msg)
        #移除句柄
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()
    def debug(self,msg):
        self.setMSG('debug',msg)
    def info(self,msg):
        self.setMSG('info',msg)
    def warning(self,msg):
        self.setMSG('warning',msg)
    def error(self,msg):
        self.setMSG('error',msg)
# if __name__ == '__main__':
#     l = Log()
#     l.info('start api')