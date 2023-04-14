"""订单支付"""
import logging
import time
import unittest

from base.base import switch_of_windows, Image_save_path
from element import tpshop
from log.tpshop_log import log_log
from page.tb_payment_of_an_order import ProxyPaymentOrder
from page.tb_personal_center import ProxyPersonalCenter
from page.tp_home import ProxyHome
from utlist import BrowserDriven


class TestPaymentOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BrowserDriven.get_driver()
        cls.home_login = ProxyHome()  # 首页
        cls.proxy_personal_center = ProxyPersonalCenter()  # 个人中心
        cls.proxy_payment_order = ProxyPaymentOrder()  # 确认支付

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        BrowserDriven.quit_driver()

    def setUp(self) -> None:
        self.driver.get(tpshop)

    def test_payment_order(self):
        self.home_login.go_tu_personal_center("我的订单")
        switch_of_windows()
        self.proxy_personal_center.proxy_obligation("待付款")
        self.proxy_personal_center.go_tu_check_the_order()
        switch_of_windows()
        self.proxy_payment_order.proxy_payment_success()
        try:
            text = self.proxy_payment_order.proxy_order_payment_success()
            log_log()
            self.assertIn("订单提交成功，我们将在第一时间给你发货", text)
        except AssertionError as a:
            Image_save_path(a)
            raise a


if __name__ == '__main__':
    unittest.main()