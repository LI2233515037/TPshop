"""添加商品到购物车"""
import time
import unittest

from base.base import Image_save_path
from element import tpshop
from page.tp_detail_page import ProxyDetailPage
from page.tp_home import ProxyHome
from page.tp_product_list import ProxyProductList
from utlist import BrowserDriven


class TestSearchForItemsToAddToCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BrowserDriven.get_driver()
        cls.home_login = ProxyHome()  # 首页
        cls.proxy_product_list = ProxyProductList()  # 列表页
        cls.proxy_detail_page = ProxyDetailPage()  # 详情页

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        BrowserDriven.quit_driver()

    def setUp(self) -> None:
        self.driver.get(tpshop)

    def test_shopping_cart(self):
        self.home_login.go_tu_detail_page("小米手机")
        self.proxy_product_list.proxy_commodity("小米手机")
        self.proxy_detail_page.proxy_add_to_shopping_cart()

        try:
            text = self.proxy_detail_page.proxy_successfully_added_text()
            self.assertIn("添加成功", text)
        except AssertionError as a:
            Image_save_path(a)
            raise a


if __name__ == '__main__':
    unittest.main()
