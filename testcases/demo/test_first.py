# -*- coding: utf-8 -
import unittest
from time import sleep
from data.data_create.data_create import Data
from common.getDriver import get_driver
from suites.demoApp.suite_login import login
from suites.demoWeb.suite_login_manage import login_manage


class Test(unittest.TestCase):
    def setUp(self):

        # 启动APP
        self.driver = get_driver('Android', 'Peso2Go', 'Reset')
        self.driver.implicitly_wait(5)  # 隐性等待,最长等5秒(因为前端全部都是整页加载,所以隐形等待即可)
        # 启动浏览器
        self.driver_manage = get_driver('Chrome')
        self.driver_manage.implicitly_wait(5)  # 隐性等待,最长等5秒(因为前端全部都是整页加载,所以隐形等待即可)

    def test_case(self):
        """APP登录-Web登录"""
        # 准备测试数据
        data = dict(Data().data_create(), **Data().data_create())
        # APP登录
        login(self.driver, data)

        # Web登录
        login_manage(self.driver_manage, data)

    def tearDown(self):
        self.driver.quit()
        self.driver_manage.quit()


if __name__ == '__main__':
    unittest.main()
