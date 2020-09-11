'''
该工具类用于找出指定目录下同一格式（时间）文件名中最新的文件(日志)
'''

import os

class NewLog:

    def __init__(self):
        pass

    @staticmethod
    def get_newLog(catalog_path):
        if catalog_path == None or catalog_path == '':
            return '访问地址为空！请确认文件地址！'

        try:
            files = os.listdir(catalog_path)
        except FileNotFoundError as fnfe:
            return print('FileNotFoundError异常：{}'.format(fnfe))
        file_names = []
        for i in files:
            file_path = os.path.join(catalog_path, i)
            if os.path.isfile(file_path):
                file_names.append(i)
        flag = True
        temp = None
        i = 0
        if file_names == []:
            return print('没有搜索到文件！')
        while flag:
            if temp == None:
                temp = file_names[i]
            else:
                if temp.split('.')[0] < file_names[i].split('.')[0]:
                    temp = file_names[i]
            i += 1
            if i == len(file_names):
                flag = False
        return temp