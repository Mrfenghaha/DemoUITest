# -*- coding: utf-8 -
from features.common.baseView import BaseView

"""
亚马逊-商品搜索列表页
"""


class ShowListPage(BaseView):

    # 点击指定商品
    def click_name_action(self, name):
        # 确定指定商品元素定位
        self.element_click_by_text(name)
        self.log('商品展示列表页,点击商品:%s' % name)

    # 点击下一页按钮
    def click_last_action(self):
        self.element_click_by_text('下一页')
        self.log('商品展示列表页,点击下一页按钮')
