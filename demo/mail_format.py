'''
邮件有两个部分：
    邮件头 邮件体（空行分隔）

        邮件头：
            每个字段（Field）包括两部分：
                字段名 字段值（冒号分隔）
                    字段：
                        Return-Path：表示退信的地址
                        Received：表示路由信息
                        Date：表示建立信件的时间
                        From：表示邮件作者（存在多个作者必须指定Sender字段）（Reply-To字段存在会使用该字段，而不会使用From）
                        Subject：邮件的主题
                        Sender：表示邮件的实际发送者
                        To：表示接受的邮件地址
                        cc：表示接受的邮件地址
                        MIME-Version：表示MIME的版本
                        Content-type：邮件内容的格式

        邮件体：
            邮件的内容（类型由邮件头Content-Type字段）（RFC 2822邮件格式，邮件体是ASCII编码的字符序列）
                MIME（Multipurpose Internet Mail Extensions）（RFC 1341）
                    MIME扩展邮件的格式，用以支持非ASCII编码的文本、非文本附件以及包含多个部分（multi-part）的邮件体等
'''