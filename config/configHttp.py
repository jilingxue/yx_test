from config import globalpara as gl
import requests
from common.Log import Log
import json

class ConfigHttp:
    def __init__(self):
        self.mylog = Log()
        self.url = None
        self.data = {}
        self.para = {}

    def set_url(self,host,url):
        '''
        配置接口的url
        '''
        self.url = host + url

    def set_data(self,data):
        '''
        配置接口的post参数
        '''
        self.data = data


    def set_para(self,para):
        '''
        配置接口的get参数
        '''
        self.para = para

    def get(self):
        '''
        重写requests  get请求
        :return:
        '''
        try:
            response = requests.get(self.url,para=json.loads(self.para))
            return response
        except Exception as e:
            self.mylog.error('接口请求异常')
            #raise e

    def post(self):
        '''
        重写requests  post请求
        :return:
        '''
        try:
            response = requests.post(self.url,data=json.loads(self.data))
            #self.mylog.info('request '+self.url)
            return response
        except Exception as e :
            self.mylog.error('接口请求错误')
            #raise e

