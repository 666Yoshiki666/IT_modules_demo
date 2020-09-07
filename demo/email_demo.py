# -*- coding: utf-8 -*-
'''
@author: Leo
@software: pycharm
@file: 111.py
@time: 2020/4/26 0026 1:13
@Desc:
'''
__author__ = 'Leo'
# -*- coding: utf-8 -*-
'''
@author: Leo
@software: pycharm
@file: send_email.py
@time: 2020/4/25 0025 22:02
@Desc:

'''
__author__ = 'Leo'

# 导入发送邮件模块:smtplib
import smtplib
# 导入构造邮件模块:MIMEText
from email.mime.text import MIMEText


class SendEmail(object):
    """
    发送邮件模块
    """

    def __init__(self):
        """
        初始化邮件配置服务
        """
        self.send_user = 'yuyang.liu@ziyun-cloud.com'
        self.mail_host = 'smtp-n.global-mail.cn'
        self.password = 'Lyy1234567'

    def send_mail(self, user_lists, subject, content):
        """
        执行发送邮件
        """
        user = "发件人名称" + "<" + self.send_user + ">"
        message = MIMEText(content, _subtype="plain", _charset="utf8")
        message['Subject'] = subject
        message['From'] = user
        message['To'] = ";".join(user_lists)
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.send_user, self.password)
            # as_string将MIMEText对象转成str
            server.sendmail(user, user_lists, message.as_string())
            server.close()
            print("邮件发送成功".center(60, '='))

        except:
            print("邮件发送失败".center(60, '='))
            raise

    def send_content(self, data):
        """
        发送邮件内容
        """
        pass_cases_nums = int(len(data['pass_cases']))
        print("用例执行成功数:%s" % pass_cases_nums)
        fail_cases_nums = int(len(data['fail_cases']))
        print("用例执行失败数:%s" % fail_cases_nums)
        not_execute_nums = int(len(data['not_execute_cases']))
        print("用例未执行数:%s" % fail_cases_nums)
        execute_num = float(pass_cases_nums + fail_cases_nums)
        total_cases = float(pass_cases_nums + fail_cases_nums + not_execute_nums)
        pass_ratio = "%.2f%%" % (pass_cases_nums / total_cases * 100)
        fail_ratio = "%.2f%%" % (fail_cases_nums / total_cases * 100)

        user_lists = ['###']
        subject = "【接口自动化测试用例执行统计】"
        content = "一共 %f 个用例, 执行了 %f 个用例，未执行 %f 个用例；成功 %f 个，通过率为 %s；失败 %f 个，失败率为 %s" % (
        total_cases, execute_num, not_execute_nums, pass_cases_nums, pass_ratio, fail_cases_nums, fail_ratio)

        self.send_mail(user_lists, subject, content)


if __name__ == '__main__':
    sm = SendEmail()
    a = ['lyyenjoyparkchoah@126.com']
    sm.send_mail(a, '收到你啦', '都懒得离开')