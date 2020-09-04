try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class ETXML:

    def __init__(self):

        tree = ET.ElementTree(file='D://pycharm//IT_modules_demo//files//sql.xml')
        root = tree.getroot()