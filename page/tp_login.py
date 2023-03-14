from base.base import BasePage, BaseHandle
from element import login_username, login_password, login_code, login_submit, wrong_password
from utlist import BrowserDriven


class PageLogin(BasePage):
    def __init__(self):
        super().__init__()
        self.login_username = login_username  # 用户名
        self.login_password = login_password  # 密码
        self.login_code = login_code  # 验证码
        self.login_submit = login_submit  # 登录按钮\
        self.wrong_password = wrong_password

    def page_login_username(self):
        return self.position_element(self.login_username)

    def page_login_password(self):
        return self.position_element(self.login_password)

    def page_login_code(self):
        return self.position_element(self.login_code)

    def page_login_submit(self):
        return self.position_element(self.login_submit)
    def page_wrong_password(self):
        return self.position_element(self.wrong_password)


class HandleLogin(BaseHandle):
    def __init__(self):
        self.handle_login = PageLogin()

    def handle_login_username(self, username):
        self.base_import(self.handle_login.page_login_username(), username)

    def handle_login_password(self, password):
        self.base_import(self.handle_login.page_login_password(), password)

    def handle_login_code(self, code):
        self.base_import(self.handle_login.page_login_code(), code)

    def handle_login_submit(self):
        self.base_click(self.handle_login.page_login_submit())
    def handle_wrong_password(self):
        # driver = BrowserDriven.get_driver()
        # return driver.switch_to.alert(self.handle_login.page_wrong_password()).text
        return self.handle_login.page_wrong_password().text


class ProxyLogin(object):
    def __init__(self):
        self.proxy_login = HandleLogin()

    def go_to_home(self, username, password, code):
        self.proxy_login.handle_login_username(username)
        self.proxy_login.handle_login_password(password)
        self.proxy_login.handle_login_code(code)
        self.proxy_login.handle_login_submit()
    def get_the_text(self):
        return self.proxy_login.handle_wrong_password()
