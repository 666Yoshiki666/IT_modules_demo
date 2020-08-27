'''
#配置文件数据读取
    1.os获取文件真实地址
    2.configparser获取配置信息
    3.configparser的get()获取需要的数据
'''

import os #操作目录文件
import codecs #编码转换
import configparser #配置文件读取写入(配置解析器)

'''
.realpath() #获取真实地址
.join() #连接两个及以上路径
'''
#获取config文件所在目录
real_catalogue = os.path.realpath(path='D:\pycharm\IT_modules_demo')
#获取config文件地址
target_file = os.path.join(real_catalogue, 'config')

class ReadConfig:

    #初始化配置解析器及读取配置信息
    def __init__(self):
        '''
        #打开config文件，返回 流
        file_stream = open(file=target_file, mode='r', encoding='UTF-8')
        #读取config信息
        data = file_stream.read()
        #校验config数据编码格式
        if data != codecs.BOM_UTF8:
            #codecs方式打开文件
            file_data = codecs.open(filename=target_file, mode='w', encoding='UTF-8')
            #写入UTF-8编码格式数据
            file_data.write(data)
            #关闭操作文件
            file_data.close()
        #关闭文件
        file_stream.close()
        '''
        #初始化配置解析器
        self.cp = configparser.ConfigParser()
        #读取配置文件
        self.cp.read(filenames=target_file, encoding='UTF-8')

    '''
    .sections()：获取section返回list，即配置文件[]内容
    .options('section名')：获取section下的option返回list，即section下的key
    .items('section名')：获取section下的键值对返回list
    .get('section名', 'option名')：获取对应value
    '''
    #获取mysql指定参数值
    def get_DB(self, name):
        value = self.cp.get(section='DATABASE', option=name)
        return value

    #获取url指定参数值
    def get_HTTP(self, name):
        value = self.cp.get(section='HTTP', option=name)
        return value

    #获取email指定参数值
    def get_EMAIL(self, name):
        value = self.cp.get(section='EMAIL', option=name)
        return value