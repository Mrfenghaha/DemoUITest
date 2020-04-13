# -*- coding: utf-8 -
from features.common.baseView import BaseView, By
"""
首页 页面元素和操作(Home)
"""


class HomePage(BaseView):
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
        self.element_click(self.personal_type)
        self.log('home页面,点击个人中心按钮')

    # 点击apply按钮
    def click_apply_action(self):
        self.element_click(self.apply_type)
        self.log('home页面,点击apply按钮')

    # 放款成功，app首页，点击PayNow按钮
    def click_paynow_action(self):
        self.element_click(self.paynow_type)
        self.log('home页面,点击PayNow按钮')

    # 放款成功，app首页，点击Extend按钮
    def click_extend_action(self):
        self.element_click(self.extend_type)
        self.log('home页面,点击Extend按钮')
