# -*- coding: utf-8 -
from common.baseView import Common
from selenium.webdriver.common.by import By
"""
首页 页面元素和操作(Home)
"""


class HomePage(Common):
    # 个人中心按钮
    personal_type = (By.ID, 'NavsIcon')
    # apply按钮
    apply_type = (By.ID, 'submit')
    # PayNow按钮
    paynow_type = (By.ID, 'PayNow')
    # Extend按钮
    extend_type = (By.ID, 'Extend')

    # 点击个人中心按钮
    def click_personal_action(self):
        self.find_element(*self.personal_type).click()
        self.log.info('home页面,点击个人中心按钮')

    # 点击apply按钮
    def click_apply_action(self):
        self.find_element(*self.apply_type).click()
        self.log.info('home页面,点击apply按钮')

    # 放款成功，app首页，点击PayNow按钮
    def click_paynow_action(self):
        self.find_element(*self.paynow_type).click()
        self.log.info('home页面,点击PayNow按钮')

    # 放款成功，app首页，点击Extend按钮
    def click_extend_action(self):
        self.find_element(*self.extend_type).click()
        self.log.info('home页面,点击Extend按钮')
