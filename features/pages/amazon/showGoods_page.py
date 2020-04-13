# -*- coding: utf-8 -
from features.common.baseView import BaseView, By
"""
亚马逊-商品详情展示页
"""


class ShowGoodsPage(BaseView):

    # 添加购物车
    add_type = (By.ID, "add-to-cart-button")
    # # 商品价格
    # price_type = (By.ID, "priceblock_ourprice")

    # 点击搜索按钮
    def click_add_action(self):
        self.element_click(self.add_type)
        self.log('商品展示页,点击添加购物车')
