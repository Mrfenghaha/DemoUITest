# -*- coding: utf-8 -
import unittest
from common.getDriver import get_driver
from common.baseView import Common
from tests.page.amazon.page_home import HomePage
from tests.page.amazon.page_show_list import ShowListPage
from tests.page.amazon.page_show_goods import ShowGoodsPage
from tests.page.amazon.page_add_success import AddSuccessPage
from tests.suite.amazon.find_goods import find_goods


class Test(unittest.TestCase):
    def setUp(self):  # unittest的格式用于以下每个用例的前提(以下用例每次执行前均会执行该方法)
        self.driver = get_driver('Chrome')  # 启动chrome浏览器
        self.driver.implicitly_wait(5)  # 隐性等待,最长等5秒

    def test_case(self):
        """访问亚马逊网站-搜索商品-找到指定商品-加入购物车"""
        # 准备测试数据
        url = 'https://www.amazon.cn/'
        search_text = '牙刷'
        books_name = '惠百施 熊本熊 成人牙刷 （颜色随机）'
        success_text = '商品已加入购物车'
        price = '￥ 83.07'

        # 打开亚马逊网页
        Common(self.driver).get(url)
        # 搜索框输入搜索内容
        HomePage(self.driver).send_search_action(search_text)
        # 点击搜索按钮
        HomePage(self.driver).click_submit_action()

        # 判断需要的商品是否存在于当前页,不存在即翻页寻找,直至找到或到达第10页仍未找到
        name_type = Common(self.driver).get_element(books_name)
        find_goods(self.driver, name_type)

        # 点击图书
        ShowListPage(self.driver).click_name_action(books_name)
        # 由于点击商品会打开一个新的窗口，所以需要切换浏览器窗口
        Common(self.driver).switch_tab(2)
        # 点击加入购物车
        ShowGoodsPage(self.driver).click_add_action()

        # 校验检查点

        # 断言提示文本(判断提示文案是100%符合)
        text_type = AddSuccessPage(self.driver).get_add_success()
        self.assertEqual(text_type, success_text)

        # 断言价格(价格需要100%符合)
        amount = AddSuccessPage(self.driver).get_amount()
        self.assertEqual(amount, price)

    def tearDown(self):  # unittest的格式用于以下每个用例的处理(以下用例每次执行后均会执行该方法)
        self.driver.quit()  # 关闭浏览器


if __name__ == '__main__':
    unittest.main()
