"""订单支付"""
from TPshop_front_desk.base.base import BasePage, BaseHandle
from TPshop_front_desk.element import pay_on_delivery, Confirm_payment_method, order_payment_success


class PagePaymentOrder(BasePage):
    def __init__(self):
        super().__init__()
        self.pay_on_delivery = pay_on_delivery  # 货到付款
        self.Confirm_payment_method = Confirm_payment_method  # 确认支付方式
        self.order_payment_success = order_payment_success  # 支付成功文案

    def page_pay_on_delivery(self):
        return self.position_element(self.pay_on_delivery)

    def page_Confirm_payment_method(self):
        return self.position_element(self.Confirm_payment_method)

    def page_order_payment_success(self):
        return self.position_element(self.order_payment_success)


class HandlePaymentOrder(BaseHandle):
    def __init__(self):
        self.handle_payment_order = PagePaymentOrder()

    def handle_pay_on_delivery(self):
        self.base_click(self.handle_payment_order.page_pay_on_delivery())

    def handle_Confirm_payment_method(self):
        self.base_click(self.handle_payment_order.page_Confirm_payment_method())

    def handle_order_payment_success(self):
        return self.handle_payment_order.page_order_payment_success().text


class ProxyPaymentOrder():
    def __init__(self):
        self.proxy_payment_order = HandlePaymentOrder()

    def proxy_payment_success(self):  # 支付成功
        self.proxy_payment_order.handle_pay_on_delivery()
        self.proxy_payment_order.handle_Confirm_payment_method()

    def proxy_order_payment_success(self):
        return self.proxy_payment_order.handle_order_payment_success()
