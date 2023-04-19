"""列表页"""
from TPshop_front_desk.base.base import BasePage, BaseHandle, switching_forms
from TPshop_front_desk.element import commodity, shop_name, shopping_cart, successfully_added_text, successfully_added


class PageProductList(BasePage):
    def __init__(self):
        super().__init__()
        self.commodity = commodity  # 点击商品
        self.shop_name = shop_name  # 积分商品列表
        self.shopping_cart = shopping_cart  # 加入购物车
        self.successfully_added_text = successfully_added_text  # 加入购物车文案

    def page_commodity(self, text):
        mag = (self.commodity[0], self.commodity[1].format(text))
        return self.position_element(mag)

    def page_shop_name(self):
        return self.position_element(self.shop_name)

    def page_shopping_cart(self):
        return self.position_element(self.shopping_cart)

    def page_successfully_added_text(self):
        return self.position_element(self.successfully_added_text)


class HandleProductList(BaseHandle):
    def __init__(self):
        self.handle_product_list = PageProductList()

    def handle_commodity(self, text):
        self.base_click(self.handle_product_list.page_commodity(text))

    def handle_shop_name(self):
        self.base_click(self.handle_product_list.page_shop_name())

    def handle_shopping_cart(self):
        self.base_click(self.handle_product_list.page_shopping_cart())

    def handle_successfully_added_text(self):
        switching_forms(successfully_added)
        return self.handle_product_list.page_successfully_added_text().text


class ProxyProductList(object):
    def __init__(self):
        self.proxy_product_list = HandleProductList()

    def proxy_commodity(self, text):
        self.proxy_product_list.handle_commodity(text)

    def proxy_shop_name(self):
        self.proxy_product_list.handle_shop_name()

    def proxy_shopping_cart(self):
        self.proxy_product_list.handle_shopping_cart()

    def proxy_successfully_added_text(self):
        return self.proxy_product_list.handle_successfully_added_text()
