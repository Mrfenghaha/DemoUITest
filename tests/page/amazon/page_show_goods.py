# -*- coding: utf-8 -
from common.baseView import Common
from common.getDriver import log
from selenium.webdriver.common.by import By
"""
亚马逊-商品详情展示页
"""


class ShowGoodsPage(Common):

    # 添加购物车
    add_type = (By.ID, "add-to-cart-button")
    # # 商品价格
    # price_type = (By.ID, "priceblock_ourprice")

    # 点击搜索按钮
    def click_add_action(self):
        self.find_element(*self.add_type).click()
        log.info('商品展示页,点击添加购物车')
