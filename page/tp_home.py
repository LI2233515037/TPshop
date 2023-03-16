"""首页"""
from base.base import BasePage, BaseHandle
from element import home_login, search_button, input_box, shopping_trolley, my_order


class PageHome(BasePage):
    def __init__(self):
        super().__init__()
        self.home_login = home_login  # 登录
        self.input_box = input_box  # 搜索框
        self.search_button = search_button  # 搜索按钮
        self.shopping_trolley = shopping_trolley  # 购物车
        self.my_order = my_order  # 我的订单

    def page_home_login(self):
        return self.position_element(self.home_login)

    def page_input_box(self):
        return self.position_element(self.input_box)

    def page_search_button(self):
        return self.position_element(self.search_button)

    def page_shopping_trolley(self):
        return self.position_element(self.shopping_trolley)

    def page_my_order(self):
        return self.position_element(self.my_order)


class HandleHome(BaseHandle):
    def __init__(self):
        self.handle_home = PageHome()

    def handle_home_login(self):
        self.base_click(self.handle_home.page_home_login())

    def handle_input_box(self, text):
        self.base_import(self.handle_home.page_input_box(), text)

    def handle_search_button(self):
        self.base_click(self.handle_home.page_search_button())

    def handle_shopping_trolley(self):
        self.base_click(self.handle_home.page_shopping_trolley())

    def handle_my_order(self):
        self.base_click(self.handle_home.page_my_order())


class ProxyHome(object):
    def __init__(self):
        self.proxy_home = HandleHome()

    def go_tu_login(self):  # 跳转登录页面
        self.proxy_home.handle_home_login()

    def go_tu_detail_page(self, text):  # 跳转详情页
        self.proxy_home.handle_input_box(text)
        self.proxy_home.handle_search_button()

    def go_tu_shopping_trolley(self):  # 跳转购物车页面
        self.proxy_home.handle_shopping_trolley()

    def go_tu_personal_center(self):  # 跳转个人中心
        self.proxy_home.handle_my_order()
