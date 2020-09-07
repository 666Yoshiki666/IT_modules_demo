'''
#发送邮件
    1.获取邮件信息
    2.获取发送信息
    3.发送指定人员
'''

import os #操作系统目录文件
import glob
import smtplib #发送邮件
import zipfile
import threading #线程
from datetime import datetime
#email库构建邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from modules.readConfig import ReadConfig
from modules.logManagement import LogInstrument

class Email:

    def __init__(self):
        rc = ReadConfig()
        global send, title, reception, text, result_path, host, user, password
        #获取发送者信息
        send = rc.get_EMAIL('from')
        #获取邮件标题
        title = rc.get_EMAIL('subject')
        #获取接收者信息
        reception = rc.get_EMAIL('to')
        #
        text = rc.get_EMAIL('text')
        #
        host = rc.get_EMAIL('host_qqy')
        #
        user = rc.get_EMAIL('user')
        #
        password = rc.get_EMAIL('pass_qqy')
        #获取结果日志所在目录
        real_catalogue = os.path.realpath(path='D:\pycharm\IT_modules_demo')
        result_path = os.path.join(real_catalogue, 'result')
        #
        self.logger = LogInstrument.get_log().logger
        #初始化邮件头字段基类
        self.msg = MIMEMultipart()

    def config_header(self):
        #邮件发送时间
        self.msg['Data'] = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        self.msg['From'] = send
        self.msg['Subject'] = title
        self.msg['To'] = ', ' + reception

    def config_content(self):
        content_plain = MIMEText(_text=text, _charset='UTF-8')
        #将给定的有效负载添加到当前有效负载
        self.msg.attach(content_plain)

    def config_file(self):
        if os.path.isfile(path=result_path) and not os.stat(path=result_path):
            return True
        else:
            return False

    def send_email(self):
        self.config_header()
        self.config_content()
        self.config_file()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host=host)
            smtp.login(user=user, password=password)
            smtp.sendmail(from_addr=send, to_addrs=None, msg=self.msg.as_string())
            smtp.quit()
            self.logger.info('测试报告已通过电子邮件发送给开发人员啦~')
        except Exception as ex:
            self.logger.error('邮件发送失败！报异常：{}'.format(str(ex)))

class EMailInstrument:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():
        if EMailInstrument.email is None:
            EMailInstrument.mutex.acquire()
            EMailInstrument.email = Email()
            EMailInstrument.mutex.release()
        return EMailInstrument.email