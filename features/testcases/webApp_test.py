# -*- coding: utf-8 -
import unittest
from data.dataCreate import DataCreate
from common.getDriver import get_driver
from features.suites.demoApp.login_suite import login


class Test(unittest.TestCase):
    def setUp(self):

        # 启动APP
        self.driver = get_driver('Android', 'Reset')
        # 启动浏览器
        self.driver_manage = get_driver('Chrome')

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
