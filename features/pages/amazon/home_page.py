# -*- coding: utf-8 -
from features.element.baseView import BaseView, By
"""
亚马逊首页
"""


class HomePage(BaseView):

    # 搜索输入框定位
    search_type = (By.ID, 'twotabsearchtextbox')
    # 搜索按钮定位
    submit_type = (By.XPATH, '//*[@id="nav-search"]/form/div[2]/div/input')

    # 点击搜索输入框并输入
    def send_search_action(self, text):
        self.element_input(self.search_type, text)
        self.log('亚马逊中国首页,点击搜索输入框并输入:%s' % text)

    # 点击搜索按钮
    def click_submit_action(self):
        self.element_click(self.submit_type)
        self.log('亚马逊中国首页,点击搜索按钮')
