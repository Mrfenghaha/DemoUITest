# -*- coding: utf-8 -
from features.element.baseView import BaseView, By
"""
亚马逊-添加商品入购物车成功页
"""


class AddSuccessPage(BaseView):

    # 添加购物车成功提示定位
    add_success_type = (By.ID, 'huc-v2-order-row-confirm-text')
    # 金额提示定位
    amount_type = (By.XPATH, '//*[@id="hlb-subcart"]/div[1]/span/span[2]')

    # 获取添加成功提示文本
    def get_add_success(self):
        return self.element_get_text(self.add_success_type)

    # 获取金额文本
    def get_amount(self):
        return self.element_get_text(self.amount_type)
