# #email下的mime包
# from email.mime.base import MIMEBase #MIME专门化的基类
# from email.mime.multipart import MIMEMultipart #MIME多部件/*类型消息的基类
# '''
# MIME邮件中各种不同类型的内容是分段存储的，各个段的排列方式、位置信息都通过Content-Type域的multipart类型来定义
#     multipart类型主要有三种子类型（_subtype）：
#         mixed：邮件含有附件
#         alternative：邮件传送超文本内容
#         related：邮件含有附件，同时可以将其它内容以内嵌资源的方式存储在邮件中
# '''
# from email.mime.nonmultipart import MIMENonMultipart #MIME非多部件类型消息的基类
# from email.mime.text import MIMEText #表示文本/*类型的MIME文档的类
# from email.mime.image import MIMEImage #表示图片/*类型的MIME文档的类
# from email.mime.audio import MIMEAudio #表示音频/*类型的MIME文档的类
# from email.mime.message import MIMEMessage #表示消息/* MIME文档的类
# from email.mime.application import MIMEApplication #表示应用程序/*类型的MIME文档的类
#
# '''
# policy #用于与新政策关联
# message #电子邮件包对象模型的基本消息对象
# '''
# #email下的py文件
# from email import message, \
#     charset, \
#     parser, \
#     header, \
#     contentmanager, \
#     encoders, \
#     errors, \
#     feedparser, \
#     generator, \
#     headerregistry, \
#     iterators, \
#     policy, \
#     utils