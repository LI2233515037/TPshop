"""直接购买商品"""
import unittest

from base.base import Image_save_path
from element import tpshop
from page.tp_home import ProxyHome
from page.tp_product_list import ProxyProductList
from utlist import BrowserDriven


class TestDirectPurchaseOfGoods(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BrowserDriven.get_driver()
        cls.proxy_home = ProxyHome()
        cls.proxy_product_list = ProxyProductList()

    @classmethod
    def tearDownClass(cls) -> None:
        BrowserDriven.quit_driver()

    def setUp(self) -> None:
        self.driver.get(tpshop)

    def test_direct_purchase_goods(self):
        self.proxy_home.go_tu_women_wear()
        self.proxy_product_list.proxy_shopping_cart()
        try:
            text = self.proxy_product_list.proxy_successfully_added_text()
            self.assertIn("添加成功",text)
        except AssertionError as a:
            Image_save_path(a)
            raise a


if __name__ == '__main__':
    unittest.main()
