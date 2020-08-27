from modules import readConfig
from modules import configHttp
from modules.common import GainData

if __name__ == '__main__':
    gainData = GainData()
    gainData.get_xml(xml_file='sql.xml')