# -*- coding: utf-8 -
from common.baseView import Common
from selenium.webdriver.common.by import By
"""
登录 页面元素和操作(Login)
"""


class LoginPage(Common):

    # 帐号输入框
    account_type = (By.ID, 'login-name-ipt')
    # 密码输入框按钮
    password_type = (By.ID, 'login-psw-ipt')
    # 登录按钮
    login_type = (By.ID, 'login-sub-btn')

    # 点击帐号输入框
    def send_personal_action(self, account):
        self.find_element(*self.account_type).clear()
        self.find_element(*self.account_type).send_keys(account)
        self.log.info('login页面,点击帐号输入框输入' + account)

    # 点击密码输入框
    def send_apply_action(self, password):
        self.find_element(*self.password_type).clear()
        self.find_element(*self.password_type).send_keys(password)
        self.log.info('login页面,点击密码输入框输入' + password)

    # 点击登录
    def click_login_action(self):
        self.find_element(*self.login_type).click()
        self.log.info('login页面,点击submit按钮')


# login页面常用操作
class LoginDefault(LoginPage):

    # 登录
    def management_login(self, account, password):
        # 输入帐号
        self.send_personal_action(account)
        # 输入密码
        self.send_apply_action(password)
        # 点击登录按钮
        self.click_login_action()
