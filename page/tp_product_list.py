"""列表页"""
from base.base import BasePage, BaseHandle
from element import commodity, shop_name


class PageProductList(BasePage):
    def __init__(self):
        super().__init__()
        self.commodity = commodity  # 点击商品
        self.shop_name = shop_name  # 积分商品列表

    def page_commodity(self, text):
        mag = (self.commodity[0], self.commodity[1].format(text))
        return self.position_element(mag)

    def page_shop_name(self):
        return self.position_element(self.shop_name)


class HandleProductList(BaseHandle):
    def __init__(self):
        self.handle_product_list = PageProductList()

    def handle_commodity(self, text):
        self.base_click(self.handle_product_list.page_commodity(text))

    def handle_shop_name(self):
        self.base_click(self.handle_product_list.page_shop_name())


class ProxyProductList(object):
    def __init__(self):
        self.proxy_product_list = HandleProductList()

    def proxy_commodity(self, text):
        self.proxy_product_list.handle_commodity(text)

    def proxy_shop_name(self):
        self.proxy_product_list.handle_shop_name()
