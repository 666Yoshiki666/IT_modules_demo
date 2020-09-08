'''
#日志工具类
    1.Log类创建(初始化)日志程序
    2.LogInstrument类创建可调用log程序
'''

import logging #自定义日志
import os
import threading #线程
from datetime import datetime
from modules import readConfig

class Log:

    #日志程序生成
    def __init__(self):
        global log_path, result_path
        #获取测试结果存放总目录
        result_path = os.path.join(readConfig.real_catalogue, 'result')
        #判断测试结果存放总目录是否不存在
        if not os.path.exists(result_path):
            #创建result目录
            os.mkdir(result_path)
        #获取测试结果存放分目录
        log_path = os.path.join(result_path, str(datetime.now().strftime('%Y%m%d')))
        #判断测试结果存放分目录是否不存在
        if not os.path.exists(log_path):
            #创建分目录
            os.mkdir(log_path)

        #创建日志程序
        self.logger = logging.getLogger()
        #设置日志等级
        self.logger.setLevel(level=logging.INFO)
        '''
        #logging模块定义的日志级别
            DEBUG #最详细的日志信息，典型应用场景是 问题诊断
            INFO #信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
            WARNING #当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
            ERROR #由于一个更严重的问题导致某些功能不能正常运行时记录的信息
            CRITICAL #当发生严重错误，导致应用程序不能继续运行时记录的信息
        日志等级：DEBUG < INFO < WARNING < ERROR < CRITICAL
        日志信息量：DEBUG > INFO > WARNING > ERROR > CRITICAL
        '''
        #创建文件处理程序
        handler = logging.FileHandler(filename=os.path.join(log_path, str(datetime.now().strftime('%Y%m%d%H%M%S') + '.log')))
        #创建格式化程序，即日志打印信息
        formatter = logging.Formatter(fmt='%(asctime)s => %(name)s => %(levelname)s => %(message)s', datefmt='%Y/%m/%d-%H:%M:%S')
        #文件处理程序设置格式化程序
        handler.setFormatter(fmt=formatter)
        #日志程序添加文件处理程序
        self.logger.addHandler(hdlr=handler)

class LogInstrument:

    #日志程序变量
    log = None

    #创建线程lock锁
    mutex = threading.Lock()

    def __init__(self):
        pass

    #创建日志程序
    @staticmethod
    def get_log():
        #判断log是否为None
        if LogInstrument.log is None:
            #线程锁定log工具类
            LogInstrument.mutex.acquire()
            #生成日志程序
            LogInstrument.log = Log()
            #log工具类释放锁
            LogInstrument.mutex.release()
        return LogInstrument.log