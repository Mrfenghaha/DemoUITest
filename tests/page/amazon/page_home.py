# -*- coding: utf-8 -
from common.baseView import Common
from common.getDriver import log
from selenium.webdriver.common.by import By
"""
亚马逊首页
"""


class HomePage(Common):

    # 搜索输入框定位
    search_type = (By.ID, 'twotabsearchtextbox')
    # 搜索按钮定位
    submit_type = (By.XPATH, '//*[@id="nav-search"]/form/div[2]/div/input')

    # 点击搜索输入框并输入
    def send_search_action(self, text):
        self.find_element(*self.search_type).send_keys(text)
        log.info('亚马逊中国首页,点击搜索输入框并输入:' + text)

    # 点击搜索按钮
    def click_submit_action(self):
        self.find_element(*self.submit_type).click()
        log.info('亚马逊中国首页,点击搜索按钮')
