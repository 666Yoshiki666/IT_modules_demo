'''
邮件有两个部分：
    邮件头 邮件体（空行分隔）

        邮件头：
            每个字段（Field）包括两部分：
                字段名 字段值（冒号分隔）
                    字段：
                        Return-Path：该字段由信息的最后发送者添加,是关于信息原始来源的地址和回朔路径
                        Received：由每个中继服务站添加，用于帮助追踪传输中出现的错误
                        Date：
                        From：邮件作者（存在多个作者必须指定Sender字段）（Reply-To字段存在会使用该字段，而不会使用From）
                        Subject：
                        Sender：邮件发送者
                        To：
                        Cc：
                        MIME-Version：
                        Content-type：
                        Bcc：

        邮件体：
            邮件的内容（类型由邮件头Content-Type字段）（RFC 2822邮件格式，邮件体是ASCII编码的字符序列）
                MIME（Multipurpose Internet Mail Extensions）（RFC 1341）
                    MIME扩展邮件的格式，用以支持非ASCII编码的文本、非文本附件以及包含多个部分（multi-part）的邮件体等
'''