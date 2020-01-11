# -*- coding: utf-8 -
from common.baseView import Common
from common.getDriver import log
from selenium.webdriver.common.by import By
"""
亚马逊-商品搜索列表页
"""


class ShowListPage(Common):

    # 点击指定商品
    def click_name_action(self, name):
        # 确定指定商品元素定位
        name_type = self.get_element(name)
        self.find_element(*name_type).click()
        log.info('商品展示列表页,点击商品:' + name)

    # 点击下一页按钮
    def click_last_action(self):
        last_type = self.get_element('下一页')
        self.find_element(*last_type).click()
        log.info('商品展示列表页,点击下一页按钮')
