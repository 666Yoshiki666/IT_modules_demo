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
from modules.most_new_log import NewLog
from modules.readConfig import ReadConfig
from modules.logManagement import LogInstrument

class Email:

    def __init__(self):
        rc = ReadConfig()
        global send, title, reception, text, result_path, host, port, user, password, send_file_path
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
        port = rc.get_EMAIL('port')
        #
        user = rc.get_EMAIL('user_qqy')
        #
        password = rc.get_EMAIL('pass_qqy')
        #获取结果日志所在目录
        real_catalogue = os.path.realpath(path='D:\pycharm\IT_modules_demo')
        time_now = datetime.now().strftime('%Y%m%d')
        result_path = os.path.join(real_catalogue, 'result', time_now)
        #需要发送文件地址
        new_file = NewLog().get_newLog(catalog_path=result_path)
        if new_file == None or new_file == '':
            send_file_path = None
        else:
            send_file_path = os.path.join(result_path, new_file)
        #
        self.logger = LogInstrument.get_log().logger
        #初始化邮件头字段基类
        self.msg = MIMEMultipart()

    #邮件头信息
    def config_header(self):
        #邮件发送时间
        self.msg['Data'] = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        self.msg['From'] = send
        self.msg['Subject'] = title
        self.msg['To'] = reception

    #添加需要发送的信息
    def config_content(self):
        content_plain = MIMEText(_text=text, _charset='UTF-8')
        #附件
        new_file = None
        if send_file_path == None:
            new_file = '附件不存在！'
        else:
            new_file = open(file=send_file_path, mode='rb').read()
        accessory = MIMEText(_text=new_file, _subtype='BASE64', _charset='UTF-8')
        accessory['Content-Type'] = 'application/octet-stream'
        accessory['Content-Disposition'] = 'attachment;filename="logo.log"'
        #将给定的有效负载添加到当前有效负载（即添加邮件体信息）
        self.msg.attach(content_plain)
        self.msg.attach(accessory)

    #判断文件是否存在
    def config_file(self):
        if os.path.isfile(path=result_path) and not os.stat(path=result_path):
            return True
        else:
            return False

    #发送邮件
    def send_email(self):
        self.config_header()
        self.config_content()
        self.config_file()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host=host, port=port)
            smtp.login(user=user, password=password)
            smtp.sendmail(from_addr=send, to_addrs=reception, msg=self.msg.as_string())
            smtp.quit()
            self.logger.info('测试报告已通过电子邮件成功发送啦~')
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