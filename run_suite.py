import unittest

from case.test_login import TestLogin
from case.test_search_for_items_to_add_to_cart import TestSearchForItemsToAddToCart
from case.test_shopping_cart_submits_orders import TestShoppingCartSubmitsOrders
from utlist import BrowserDriven

unit = unittest.TestSuite()
runner = unittest.TextTestRunner()
BrowserDriven.driver_exit_status(False)

unit.addTest(unittest.makeSuite(TestLogin))  # 登录
unit.addTest(unittest.makeSuite(TestSearchForItemsToAddToCart))  # 添加商品到购物车
unit.addTest(unittest.makeSuite(TestShoppingCartSubmitsOrders))  # 提交订单


runner.run(unit)
BrowserDriven.driver_exit_status(True)
BrowserDriven.quit_driver()
