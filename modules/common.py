'''
#读取本地文件信息（excel、xml）
'''

import os
from xlrd import open_workbook #操作excel
try:
    from xml.etree import ElementTree #操作xml
except ImportError:
    from xml.etree import cElementTree #速度更快
from modules import readConfig

class GainData:

    def __init__(self):
        #excel文件目录
        self.file_path_catalogue = os.path.join(readConfig.real_catalogue, 'files')
        self.database ={}

    #获取excel文件测试用例（用例数据）
    def get_xls(self, xls_name, sheet_name):
        #用例数据
        cls = []
        #excel文件地址
        xls_path = os.path.join(self.file_path_catalogue, xls_name)
        #打开指定excel文件
        excel_file = open_workbook(filename=xls_path)
        '''
        #获取工作表方式
            .sheets()[0] #通过索引顺序获取
            .sheet_by_index(0) #通过索引顺序获取
            .sheet_by_name(sheet_name) #通过工作表名称获取
        '''
        #获取指定工作表
        sheet = excel_file.sheet_by_name(sheet_name=sheet_name)
        '''
            .nrows #获取工作表行数
            .ncols #获取工作表列数
        '''
        #获取行数
        nrows = sheet.nrows
        for n in range(nrows):
            '''
                row_values() #获取整行
                col_values() #获取整列
            '''
            #工作列表第一行代表属性名，所以去掉
            if n != 0:
                #获取整行数据放入集合
                cls.append(sheet.row_values(rowx=n))
        return cls

    #获取xml文件数据（sql）
    def get_xml(self, xml_file):
        if len(self.database) == 0:
            #xml文件地址
            xml_path = os.path.join(self.file_path_catalogue, xml_file)
            #解析xml文件为元素树
            tree = ElementTree.parse(source=xml_path)
            print('tree：{}'.format(tree))
            data = tree.findall(path='database')
            print('data：{}'.format(data))