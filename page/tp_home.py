from base.base import BasePage, BaseHandle
from element import home_login


class PageHome(BasePage):
    def __init__(self):
        super().__init__()
        self.home_login = home_login  # 登录

    def page_home_login(self):
        return self.position_element(self.home_login)


class HandleHome(BaseHandle):
    def __init__(self):
        self.handle_home = PageHome()

    def handle_home_login(self):
        self.base_click(self.handle_home.page_home_login())


class ProxyHome(object):
    def __init__(self):
        self.proxy_home = HandleHome()

    def go_tu_login(self):  # 跳转登录页面
        self.proxy_home.handle_home_login()
