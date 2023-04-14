"""订单详情页"""
from base.base import BasePage, BaseHandle, switching_forms, popover_content
from element import cancellation_order, whether_to_cancel_the_order


class PageOrderDetailsPage(BasePage):
    def __init__(self):
        super().__init__()
        self.cancellation_order = cancellation_order  # 取消订单
        self.whether_to_cancel_the_order = whether_to_cancel_the_order#是否取消订单

    def page_cancellation_order(self):
        return self.position_element(self.cancellation_order)
    def page_whether_to_cancel_the_order(self):
        return self.position_element(self.whether_to_cancel_the_order)


class HandleOrderDetailsPage(BaseHandle):
    def __init__(self):
        self.handle_order_details_page = PageOrderDetailsPage()

    def handle_cancellation_order(self):
        self.base_click(self.handle_order_details_page.page_cancellation_order())
    def handle_whether_to_cancel_the_order(self):
        # switching_forms("#layui-layer1")
        popover_content("#layui-layer1")
        self.base_click(self.handle_order_details_page.page_whether_to_cancel_the_order())
        popover_content("#layui-layer2")
        self.base_click(self.handle_order_details_page.page_whether_to_cancel_the_order())


class ProxyOrderDetailsPage():
    def __init__(self):
        self.proxy_order_details_page = HandleOrderDetailsPage()

    def proxy_cancellation_order(self):
        self.proxy_order_details_page.handle_cancellation_order()
        self.proxy_order_details_page.handle_whether_to_cancel_the_order()
