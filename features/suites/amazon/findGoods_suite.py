# -*- coding: utf-8 -
from features.element.baseView import BaseView
from features.pages.amazon.showList_page import ShowListPage


def find_goods_action(driver, name):
    name_type = BaseView(driver).get_element_by_text(name)
    check_result = BaseView(driver).check_element_if_exist(name_type)  # 检查元素是否存在
    a = 1
    while check_result is False:  # 当元素不存在时自动点击下一页,直到找到元素
        ShowListPage(driver).click_last_action()
        check_result = BaseView(driver).check_element_if_exist(name_type)
        a += 1
        if a >= 10:  # 由于亚马逊中国搜索后只能显示10页商品,所以翻页达到10页需要停止翻页
            print('商品不存在')
            quit()
