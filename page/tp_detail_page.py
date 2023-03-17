﻿"""商品详情页"""
from base.base import BasePage, BaseHandle, switching_forms
from element import add_to_shopping_cart, successfully_added_text, successfully_added
from utlist import BrowserDriven


class PageDetailPage(BasePage):
    def __init__(self):
        super().__init__()
        self.add_to_shopping_cart = add_to_shopping_cart  # 加入购物车
        self.successfully_added_text = successfully_added_text  # 加入购物车文本

    def page_add_to_shopping_cart(self):
        return self.position_element(self.add_to_shopping_cart)

    def page_successfully_added_text(self):
        return self.position_element(self.successfully_added_text)


class HandleDetailPage(BaseHandle):
    def __init__(self):
        self.handle_product_list = PageDetailPage()

    def handle_add_to_shopping_cart(self):
        self.base_click(self.handle_product_list.page_add_to_shopping_cart())

    def handle_successfully_added_text(self):
        switching_forms(successfully_added)
        return self.handle_product_list.page_successfully_added_text().text


class ProxyDetailPage(object):
    def __init__(self):
        self.proxy_product_list = HandleDetailPage()

    def proxy_add_to_shopping_cart(self):
        self.proxy_product_list.handle_add_to_shopping_cart()

    def proxy_successfully_added_text(self):
        return self.proxy_product_list.handle_successfully_added_text()
