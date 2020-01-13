# -*- coding: UTF-8 -*-
import yaml
import configparser
from config.cons import DATA_PATH 

class ReadYaml(object):
  

    def __init__(self):
        
        self.yaml_path=DATA_PATH 
        self.conf = configparser.ConfigParser()

    @property
    def get_datas(self):
        with open(self.yaml_path,'r')as f:
            self.content=yaml.safe_load(f)
        return self.content
    
if __name__ == "__main__":
    redy = ReadYaml()
    print(redy.get_datas)