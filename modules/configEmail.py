'''
#获取邮件
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
        global host, user, password, port, sender, title, content
        host = rc.get_EMAIL('mail_host')
        user = rc.get_EMAIL('mail_user')
        password = rc.get_EMAIL('mail_pass')
        port = rc.get_EMAIL('mail_port')
        sender = rc.get_EMAIL('sender')
        title = rc.get_EMAIL('subject')
        content = rc.get_EMAIL('content')
        value = rc.get_EMAIL('receiver')
        self.receiver = []
        for r in str(value).split('/'):
            self.receiver.append(r)
        date = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        self.subject = title + ' => ' + date
        self.log = LogInstrument.get_log()
        self.logger = self.log.logger
        self.msg = MIMEMultipart()

    def config_header(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ';'.join(self.receiver)

    def config_content(self):
        content_plain = MIMEText(content, 'plain', 'UTF-8')
        self.msg.attach(content_plain)

    def config_file(self):
        reportpath = self.log
        if os.path.isfile(path=reportpath) and not os.stat(path=reportpath):
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
            smtp.sendmail(sender,self.receiver, self.msg.as_string())
            smtp.quit()
            self.logger.info('The test report has send to developer by email.')
        except Exception as ex:
            self.logger.error(str(ex))