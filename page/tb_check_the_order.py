"""购物车页面"""
from base.base import BasePage, BaseHandle, switch_of_windows
from element import submit_order, order_submitted_successfully


class PageCheckTheOider(BasePage):
    def __init__(self):
        super().__init__()
        self.submit_order = submit_order  # 提交订单
        self.order_submitted_successfully = order_submitted_successfully#提交成功后的文案

    def page_submit_order(self):
        return self.position_element(self.submit_order)
    def page_order_submitted_successfully(self):
        return self.position_element(self.order_submitted_successfully)


class HandleCheckTheOider(BaseHandle):
    def __init__(self):
        self.handle_check_the_order = PageCheckTheOider()

    def handle_submit_order(self):
        self.base_click(self.handle_check_the_order.page_submit_order())
    def handle_order_submitted_successfully(self):
        switch_of_windows()
        return self.handle_check_the_order.page_order_submitted_successfully().text


class ProxyCheckTheOider(object):
    def __init__(self):
        self.proxy_check_the_order = HandleCheckTheOider()

    def go_to_successfully_submitted_orders(self):
        self.proxy_check_the_order.handle_submit_order()
    def proxy_order_submitted_successfully(self):
        return self.proxy_check_the_order.handle_order_submitted_successfully()
