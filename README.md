
# APITestFrameWork

    unittest+requests接口框架
    说明：

    环境需求：
        1.需安装python 3.以上版本
        2.需要安装requests库
        3.需安装unittest框架
        4.需对发送测试报告邮件的邮箱正确配置
        5.需要安装PyMySQL处理数据库
        6.使用HTMLTestRunner发送测试报告
    运行项目：
        1.下载项目到本地
        2.打开cd切换到项目根目录
        3.安装依赖pip install requirements.txt
        4.输入python runtest. 
           
## 目录结构
```

├── TestCase 测试用例
│   ├── Test_J50001_Login.py
│   ├── __init__.py
│
├── common
│   ├── __init__.py
│   ├──  HTMLTestRunner.py 
│   ├── config.py  读取ini文件数据
│   ├── db.py  数据库连接和sql封装
│   ├── parameteryaml.py  读取yaml文件数据
│   ├── sendhttp.py requests封装
│
├── config
│   ├── __init__.py
│   ├── config.ini 邮件和数据库配置
│   ├── cons.py 目录常量
│   └── logging_config.ini
│
├── datas 数据源
│   └── TestData.yaml  
│
├── report 测试报告
│   └── jing5Report.html
├── requirements.txt 
├── runtest.py  函数入口
├── README.md


```