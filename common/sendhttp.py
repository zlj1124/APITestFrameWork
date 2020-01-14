# -*- coding:UTF-8 -*-
import requests
from common.parameteryaml import ReadYaml
from functools import partial
from requests.adapters import HTTPAdapter





class Send_requset(object):
    def __init__(self):
        gt = ReadYaml()
        self.host = gt.get_datas["jing5host"]
        self.path = gt.get_datas["login_path"]
        self.host_path = "".join([self.host, self.path])
        self.headers = {
            # "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 "
                          "(Macintosh; Intel Mac OS X 10_12_6) "
            # "AppleWebKit/537.36 (KHTML, like Gecko) "
            # "Chrome/71.0.3578.98 Safari/537.36"
            }
        self.data_sucess = gt.content["data_sucess"]
        self.session=requests.Session()
        self.session.mount('http://', HTTPAdapter(max_retries=3))
        self.session.mount('https://', HTTPAdapter(max_retries=3))
        
    @property
    def send_request(self):
            
        response = requests.post(url=self.host_path,data=self.data_sucess )
        auth = "JWT " + response.json()["token"]
        self.headers["Authorization"] = auth
        # self.send_http=partial(requests.request,headers=self.headers)
        self.send_http=partial(self.session.request,headers=self.headers,timeout=3)

        
        return self.send_http
