'''
#接口访问
    1.获取访问信息
    2.访问接口
'''

import requests #访问接口
from modules import readConfig
from modules.logManagement import LogInstrument

#读取配置信息工具类
localReadConfig = readConfig.ReadConfig()

#接口访问
class ConfigHTTP:

    def __init__(self):
        global host, port, timeout
        #获取访问地址
        host = localReadConfig.get_HTTP(name='url')
        #获取访问端口
        port = localReadConfig.get_HTTP(name='port')
        #获取超时时间
        timeout = localReadConfig.get_HTTP(name='timeout')

        #获取日志程序
        self.http_logger = LogInstrument.get_log().logger

        #接口请求需要的参数
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    #get请求
    def get(self):
        try:
            response = requests.get(url=self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            return response
        except Exception as ex:
            self.http_logger.error('get请求地址：{}，请求报异常：{}'.format(self.url, ex))
            return None

    #post请求
    def post(self):
        try:
            response = requests.post(url=self.url, data=self.data, headers=self.headers, files=self.files, timeout=float(timeout))
            return response
        except Exception as ex:
            self.http_logger.error('post请求地址：{}，请求报异常：{}'.format(self.url, ex))
            return None