# -*- coding:UTF-8 -*-
import pymysql.cursors
# from import ReadConfig
from common.config import ReadConfig
db_conf= ReadConfig()


class DbConnect(object):  

    def __init__(self,section):
        db_msg=db_conf.get_option_value(section)
        self.connection = pymysql.connect(
            host= db_msg['host'],
            port= int(db_msg['port']),
            user= db_msg['user'],
            password= db_msg['password'],
            db= db_msg['db'],
            charset= db_msg['charset'],
            cursorclass=pymysql.cursors.DictCursor
            )
        self.cursor=self.connection.cursor()

    def update_sql(self, *args):
        try:
            sql = "UPDATE %s SET %s=%s WHERE %s='%s';" %(args)
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:   
            print('Error:%s'%e)
               
        
            
    def delete_sql(self, *args):
        try:
            
            sql = "DELETE FROM %s WHERE %s='%s';" %(args)
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:   
            print('Error:%s'%e)    
       
               
    def select_sql(self, *args):
        try:
            sql = "SELECT %s, %s, %s FROM %s WHERE %s='%s' ORDER BY %s DESC LIMIT 1;" %(args)
            self.cursor.execute(sql)
            self.connection.commit()
            result = self.cursor.fetchall()
            return result[0]
        except Exception as e:   
            print('Error:%s'%e)
       
          
    def close_conn(self):
        self.connection.close()
        self.cursor.close()
        

          
        

if __name__ == "__main__":
    pass











