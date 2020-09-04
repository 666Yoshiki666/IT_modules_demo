'''
#获取数据库配置连接
    1.创建数据库连接
    2.执行sql获取数据
    3.关闭数据库连接
'''

import pymysql #mysql操作
from modules.readConfig import ReadConfig
from modules.logManagement import LogInstrument

class TargetDB:

    global host, username, password, port, database, config

    rc = ReadConfig()
    host = rc.get_DB(name='host')
    username = rc.get_DB(name='username')
    password = rc.get_DB(name='password')
    port = rc.get_DB(name='port')
    database = rc.get_DB(name='database')
    config = {
        'host' : str(host),
        'user' : str(username),
        'password' : password,
        'port' : int(port),
        'database' : database
    }

    def __init__(self):
        self.logger = LogInstrument.get_log().logger
        self.db = None
        self.cursor = None

    #数据库连接
    def connectDB(self):
        try:
            #数据库连接
            self.db = pymysql.connect(**config)
            #创建游标
            self.cursor = self.db.cursor()
            print('数据库连接成功~')
        except ConnectionError as ce:
            self.logger.error('数据库连接失败！报异常：{}'.format(ce))

    #sql语句执行
    def executeSQL(self, sql, params=None):
        self.connectDB()
        #sql语句执行
        if params is None or params is '':
            self.cursor.execute(query=sql)
        else:
            self.cursor.execute(query=sql, args=params)
        #将更改提交到稳定存储，否则无法保存新建或者修改的数据
        self.db.commit()
        return self.cursor

    #sql执行获取所有数据
    def get_data_all(self, cursor):
        value = cursor.fetchall()
        return value

    #sql执行获取指定条数
    def get_data_many(self, cursor, size):
        value = cursor.fetchmany(size)
        return value

    #sql执行顺序获取1条
    def get_data_one(self, cursor):
        value = cursor.fetchone()
        return value

    #关闭数据库连接
    def closeDB(self):
        #关闭游标
        self.cursor.close()
        #关闭连接
        self.db.close()
        print('数据库连接断开~')