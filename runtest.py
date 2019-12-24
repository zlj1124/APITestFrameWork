# -*- coding:UTF-8 -*-
import os
import time
import unittest
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from common import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from common.config import ReadConfig
from multiprocessing import Pool


localconfig = ReadConfig()
# import common.variable
# import logging.config
# logging.config.fileConfig(common.variable.LOGERPATH)
# logger = logging.getLogger(__name__)


class RunFrame(object):
    def __init__(self):
        mail_msg= localconfig.get_option_value('Email')
        self.smtp_server=mail_msg['smtp_server']
        self.send_mail=mail_msg['send_mail']
        self.password=mail_msg['password']
        self.rec_mail = mail_msg["rec_mail"].split(",")
        self.subject = "接口自动化测试报告"

    def run_allcase(self,protocol,case):

        try:
            test_dir = os.path.join(os.getcwd(), "TestCase/")
            # rep_name = os.path.join(os.getcwd(), "report/Report.html")
            # new_time = time.strftime(protocol+"Rep%Y-%m-%d.html", time.localtime())
            rep_name = time.strftime(protocol+"Report.html")
            rep_dir = os.path.join(os.getcwd(), "report/")
            rep_name = rep_dir+rep_name
            file_open = open(rep_name, "wb")
            discover_test = unittest.defaultTestLoader.discover(
                test_dir, pattern=case)
            runner = HTMLTestRunner.HTMLTestRunner(
                stream=file_open, title="测试报告", description=protocol+"用例执行情况:"
            )

            runner.run(discover_test)
            file_open.close()
        except Exception as e:
            print ("running tesecase fail:", e)


    def sendmail(self,protocol):
        self.subject = protocol+self.subject
        test_dir = os.path.join(os.getcwd(), "report/")
        rep_dir= os.path.join(test_dir, protocol+'Report.html')
        with open(rep_dir, "rb") as f:
            mail_content = f.read()
           
        annex = MIMEMultipart()
        # 添加正文
        msg = MIMEText(mail_content, "html", "utf-8")
        # 添加附件
        msg_html = MIMEText(mail_content, "html", "utf-8")
        msg_html["Content-Type"] = "application/octet-stream"
        msg_html["Content-Disposition"] = "attachment; filename=Report.html"
        annex.attach(msg)
        annex.attach(msg_html)
        annex["Subject"] = Header(self.subject, "utf-8")
        annex["From"] = formataddr(["测试团队", self.send_mail])
        annex["To"] = ",".join(self.rec_mail)
        try:
            server = smtplib.SMTP_SSL(self.smtp_server, 465)
            server.login(self.send_mail, self.password)
            server.sendmail(self.send_mail, self.rec_mail, annex.as_string())
            server.quit()
        except Exception as e:
            print (e )


# def run(protocol,case):
#     send = RunFrame()
#     send.run_allcase(protocol,case)
#     send.sendmail(protocol)
  
  
if __name__ == "__main__":
    run=RunFrame()
    run.run_allcase('jing5','Test_J5*.py')
    # run.sendmail('jing5')


    # protocol_dict={
    #         'jing5':'Test_J5*.py',     
    #     }
  
    # p = Pool(processes=1)
    # for protocol,case in protocol_dict.items():
    #     p.apply_async(run, args=(protocol,case))      
    # p.close()
    # p.join()






