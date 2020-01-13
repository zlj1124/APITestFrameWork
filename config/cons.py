
from datetime import datetime
import os

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 
# 报告目录
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
# ui对象库config.ini文件所在目录
CONF_PATH = os.path.join(ROOT_DIR, 'config', 'config.ini')
DB_PATH = os.path.join(ROOT_DIR,'config','db.ini')
# 测试数据所在目录
DATA_PATH = os.path.join(ROOT_DIR, 'datas', 'TestData.yaml')
# 当前时间
CURRENT_TIME = datetime.now().strftime('%H_%M_%S')

