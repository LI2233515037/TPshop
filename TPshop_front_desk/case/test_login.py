"""登录页"""
from nose_parameterized import parameterized
import time
import unittest
from TPshop_front_desk.base.base import Image_save_path
from TPshop_front_desk.data.read_yaml import read_yaml
from TPshop_front_desk.element import tpshop
from TPshop_front_desk.page.tp_home import ProxyHome
from TPshop_front_desk.page.tp_login import ProxyLogin
from TPshop_front_desk.utlist import BrowserDriven


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BrowserDriven.get_driver()
        cls.home_login = ProxyHome()  # 跳转登录页
        cls.login = ProxyLogin()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        BrowserDriven.quit_driver()

    def setUp(self) -> None:
        self.driver.get(tpshop)
        self.home_login.go_tu_login()

    @parameterized.expand(read_yaml())
    def test_login(self, username, pwd, code, expected, success):

        self.login.go_to_home(username, pwd, code)
        if success:
            try:
                time.sleep(10)
                title = self.driver.title
                self.assertIn(expected, title)
            except AssertionError as a:
                Image_save_path(a)
                raise a
        else:
            try:
                text = self.login.get_the_text()
                self.assertIn(expected, text)
            except AssertionError as b:
                Image_save_path(b)
                raise b


if __name__ == '__main__':
    unittest.main()
