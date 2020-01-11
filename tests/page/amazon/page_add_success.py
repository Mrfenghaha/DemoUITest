# -*- coding: utf-8 -
from common.baseView import Common
from common.getDriver import log
from selenium.webdriver.common.by import By
"""
亚马逊-添加商品入购物车成功页
"""


class AddSuccessPage(Common):

    # 添加购物车成功提示定位
    add_success_type = (By.ID, 'huc-v2-order-row-confirm-text')
    # 金额提示定位
    amount_type = (By.XPATH, '//*[@id="hlb-subcart"]/div[1]/span/span[2]')

    # 获取添加成功提示文本
    def get_add_success(self):
        add_success = self.find_element(*self.add_success_type).text
        return add_success

    # 获取金额文本
    def get_amount(self):
        amount = self.find_element(*self.amount_type).text
        return amount
