# -*- coding: utf-8 -
import unittest
from data.data_create import DataCreate
from common.getDriver import get_driver
from tests.suite.demoApp.suite_login import login


class Test(unittest.TestCase):
    def setUp(self):

        # 启动APP
        self.driver = get_driver('Android', 'Reset')
        self.driver.implicitly_wait(5)  # 隐性等待,最长等5秒(因为前端全部都是整页加载,所以隐形等待即可)
        # 启动浏览器
        self.driver_manage = get_driver('Chrome')
        self.driver_manage.implicitly_wait(5)  # 隐性等待,最长等5秒(因为前端全部都是整页加载,所以隐形等待即可)

    def test_case(self):
        """APP登录-Web登录"""
        # 准备测试数据
        data = dict(DataCreate().data_create(), **DataCreate().data_create())
        # APP登录
        login(self.driver, data)

    def tearDown(self):
        self.driver.quit()
        self.driver_manage.quit()


if __name__ == '__main__':
    unittest.main()
