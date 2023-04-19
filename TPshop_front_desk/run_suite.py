import os
import time
import unittest
from HTMLTestRunnerCN import HTMLTestReportCN

from case.test_cancellation_of_order import TestCancellatinoOrder
from case.test_direct_purchase_of_goods import TestDirectPurchaseOfGoods
from case.test_login import TestLogin
from case.test_payment_of_an_order import TestPaymentOrder
from case.test_redeem_points_for_goods import TestRedeemPointsForGoods
from case.test_search_for_items_to_add_to_cart import TestSearchForItemsToAddToCart
from case.test_shopping_cart_submits_orders import TestShoppingCartSubmitsOrders
from utlist import BrowserDriven

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

unit = unittest.TestSuite()
runner = unittest.TextTestRunner()
BrowserDriven.driver_exit_status(False)

# unit.addTest(unittest.makeSuite(TestLogin))  # 登录
unit.addTest(unittest.makeSuite(TestSearchForItemsToAddToCart))  # 添加商品到购物车
unit.addTest(unittest.makeSuite(TestShoppingCartSubmitsOrders))  # 提交订单
unit.addTest(unittest.makeSuite(TestPaymentOrder))  # 订单支付
unit.addTest(unittest.makeSuite(TestRedeemPointsForGoods))  # 积分兑换商品
unit.addTest(unittest.makeSuite(TestDirectPurchaseOfGoods))  # 购买商品
unit.addTest(unittest.makeSuite(TestCancellatinoOrder))  # 取消订单
# 设置报告存放路径及文件名
report_name = BASE_DIR + '\\report\\report_{}.html'.format(time.strftime('%Y%m%d_%H%M%S'))

# 生成测试报告
with open(report_name, 'wb') as f:
    runner = HTMLTestReportCN(stream=f,
                              verbosity=2,
                              title='Web 自动化测试报告',
                              description='系统: macOS, 语言: Python, 浏览器: 谷歌浏览器',
                              tester='QA14')
    runner.run(unit)

BrowserDriven.driver_exit_status(True)
BrowserDriven.quit_driver()
