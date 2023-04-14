"""取消订单"""
import time
import unittest

from base.base import switch_of_windows
from element import tpshop
from page.tb_order_details_page import ProxyOrderDetailsPage
from page.tb_personal_center import ProxyPersonalCenter
from page.tp_home import ProxyHome
from utlist import BrowserDriven


class TestCancellatinoOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BrowserDriven.get_driver()
        cls.proxy_home = ProxyHome()#首页
        cls.proxy_personal_center = ProxyPersonalCenter()#待收货
        cls.proxy_order_details_page = ProxyOrderDetailsPage()#取消订单


    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(10)
        BrowserDriven.quit_driver()

    def setUp(self) -> None:
        self.driver.get(tpshop)
    def test_cancellation_order(self):
        self.proxy_home.go_tu_personal_center("我的订单")
        switch_of_windows()
        self.proxy_personal_center.proxy_obligation("待发货")
        self.proxy_personal_center.proxy_obligation("查看详情")
        self.proxy_order_details_page.proxy_cancellation_order()

if __name__ == '__main__':
    unittest.main()
