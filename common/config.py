# -*- coding:UTF-8 -*-
import configparser
from config.cons import CONF_PATH




class ReadConfig(object):
    """
    读取ini文件并获取ini文件中的值
    """
    def __init__(self):
        self.file=CONF_PATH
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file)
        
    
    def get_option_value(self, section):
        """获取指定section下所有的option和对应的数据，返回字典"""
        value = dict(self.conf.items(section))
        return value
    
 

if __name__ == "__main__":
    pass