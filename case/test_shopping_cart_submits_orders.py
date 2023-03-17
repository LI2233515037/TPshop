"""提交订单"""
import logging
import time
import unittest

from base.base import Image_save_path
from element import tpshop
from page.tb_check_the_order import ProxyCheckTheOider
from page.tb_shopping_trolley import ProxyShoppingTrolley
from page.tp_detail_page import ProxyDetailPage
from page.tp_home import ProxyHome
from page.tp_product_list import ProxyProductList
from utlist import BrowserDriven


class TestShoppingCartSubmitsOrders(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BrowserDriven.get_driver()
        cls.home_login = ProxyHome()  # 首页
        cls.proxy_shopping_trolley = ProxyShoppingTrolley()  # 提交订单
        cls.proxy_check_the_oider = ProxyCheckTheOider()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        BrowserDriven.quit_driver()

    def setUp(self) -> None:
        self.driver.get(tpshop)

    def test_shopping_cart_submits_orders(self):
        self.home_login.go_tu_shopping_trolley()
        time.sleep(5)
        self.proxy_shopping_trolley.go_to_check_the_order_page()
        time.sleep(10)
        self.proxy_check_the_oider.go_to_successfully_submitted_orders()
        try:
            text = self.proxy_check_the_oider.proxy_order_submitted_successfully()
            logging.info(text)
            print(text)
            self.assertIn("订单提交成功，请您尽快付款", text)
        except AssertionError as a:
            Image_save_path(a)
            raise a


if __name__ == '__main__':
    unittest.main()
