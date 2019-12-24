# -*- coding:UTF-8 -*-
import requests
import unittest
from common.parameteryaml import ReadYaml




class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        tl = ReadYaml()
        self.host = tl.get_datas["jing5host"]
        self.path = tl.get_datas["login_path"]
        self.data_sucess = tl.get_datas["data_sucess"]
        self.data_error = tl.get_datas["data_error"]
        self.data_panull = tl.get_datas["data_passnull"]
        self.data_usenull = tl.get_datas["data_usernull"]
        self.url = "".join([self.host, self.path])

    def test_a_req_post(self):
        """验证登录接口正常登录"""
        response = requests.post(self.url, data=self.data_sucess)
        self.assertNotEqual(
            response.json()["token"], "", msg="login failed"
        )

    def test_b_req_error(self):
        """验证用户名和密码错误"""
        response = requests.post(
            self.url, data=self.data_error
        )
        self.assertEqual(
            response.json()["error"], "用户名或者密码有误"
        )

    def test_c_password_null(self):
        """验证密码为空"""
        response = requests.post(
            self.url, data=self.data_panull
        )
        self.assertEqual(
            response.json()["password"], ["该字段是必填项。"]
        )

    def test_d_username_null(self):
        """验证用户名为空"""
        response = requests.post(
            self.url, data=self.data_usenull
        )
        self.assertEqual(
            response.json()["username"], ["该字段是必填项。"]
        )

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == "__main__":
    unittest.main()



