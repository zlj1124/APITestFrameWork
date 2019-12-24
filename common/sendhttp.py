# -*- coding:UTF-8 -*-
import requests
from common.parameteryaml import ReadYaml
from functools import partial




class Send_requset(object):
    def __init__(self,procotol):
        gt = ReadYaml()
        self.host = gt.content["jing5host"]
        self.path = gt.content["login_path"]
        host_path = "".join([self.host, self.path])
        self.headers = {
            # "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 "
                          "(Macintosh; Intel Mac OS X 10_12_6) "
            # "AppleWebKit/537.36 (KHTML, like Gecko) "
            # "Chrome/71.0.3578.98 Safari/537.36"
            }
        self.data_sucess = gt.content["data_sucess"]
        response = requests.post(url=host_path,data=self.data_sucess )
        auth = "JWT " + response.json()["token"]
        self.headers["Authorization"] = auth
        self.send_request=partial(requests.request,headers=self.headers)
