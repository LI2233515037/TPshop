"""积分兑换商品"""
import unittest

from element import tpshop
from page.tp_detail_page import ProxyDetailPage
from page.tp_home import ProxyHome
from page.tp_product_list import ProxyProductList
from utlist import BrowserDriven


class TestRedeemPointsForGoods(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BrowserDriven.get_driver()
        cls.proxy_home = ProxyHome()
        cls.proxy_product_list = ProxyProductList()
        cls.proxy_detail_page = ProxyDetailPage()

    @classmethod
    def tearDownClass(cls) -> None:
        BrowserDriven.quit_driver()

    def setUp(self) -> None:
        self.driver.get(tpshop)

    def test_redeen_points(self):
        self.proxy_home.go_tu_personal_center("积分商城")
        self.proxy_product_list.proxy_commodity("小熊饼干990")
        self.proxy_detail_page.proxy_exchange_immediately()

if __name__ == '__main__':
    unittest.main()