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
            #获取根节点
            root = tree.getroot()
            '''
            <page>xxx</page>这种结构称为一个element
            page称作element的tag
            <></>之间的内容称作element的text或data
            <>中的name称作element的attrib
            整个XML树被称作ElementTree
            
            root.tag #root element的tag
            root.text #root element的text
            root.attrib #root element本身的attrib,dict格式的
            root.tail #root element的tag结束到下一个tag之间的text
            
            DICT逻辑获取树形结构的text
            root[0][0][0].text
            '''
            # if str(root.text) != '' and str(root.text).isalnum():
            #     self.database[root.get(key='name')] = str(root.text)
            #     print(self.database)
            # else:
            #     print('xml文件没有可取数据！')
            '''
            .iter(tag) #遍历tree中指定tag
            .strip() #去除首尾空格
            .get(key) #当前element中获取符合指定attrib名的value
            '''
            databases = root.iter(tag='database')
            for d in databases:
                table = {}
                tables = root.iter(tag='table')
                for t in tables:
                    sql = {}
                    sqls = root.iter(tag='sql')
                    for s in sqls:
                        sql[str(s.get(key='id'))] = str(s.text).strip()
                    table[str(t.get(key='name'))] = sql
                self.database[str(d.get(key='name'))] = table
        return self.database