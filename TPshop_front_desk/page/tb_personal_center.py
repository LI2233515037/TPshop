"""个人中心"""
from TPshop_front_desk.base.base import BasePage, BaseHandle
from TPshop_front_desk.element import obligation, immediate_payment


class PagePersonalCenter(BasePage):
    def __init__(self):
        super().__init__()
        self.obligation = obligation  # 订单状态
        self.immediate_payment = immediate_payment  # 立即支付

    def page_obligation(self, text):
        order_status = (self.obligation[0], self.obligation[1].format(text))
        return self.position_element(order_status)

    def page_immediate_payment(self):
        return self.position_element(self.immediate_payment)


class HandlePersonalCenter(BaseHandle):
    def __init__(self):
        self.handle_personal_center = PagePersonalCenter()

    def handle_obligation(self, text):
        self.base_click(self.handle_personal_center.page_obligation(text))

    def handle_immediate_payment(self):
        self.base_click(self.handle_personal_center.page_immediate_payment())


class ProxyPersonalCenter(object):
    def __init__(self):
        self.proxy_personal_center = HandlePersonalCenter()

    def proxy_obligation(self, text):  # 订单状态
        self.proxy_personal_center.handle_obligation(text)

    def go_tu_check_the_order(self):#立即支付
        self.proxy_personal_center.handle_immediate_payment()
