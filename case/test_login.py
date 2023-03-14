from nose_parameterized import parameterized
import time
import unittest

from base.base import popover_content
from data.read_yaml import read_yaml
from element import tpshop
from page.tp_home import ProxyHome
from page.tp_login import ProxyLogin
from utlist import BrowserDriven


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
            except Exception as a:
                self.driver.get_screenshot_as_file("E:\\项目01\\TPshop\\screenshot\\{}_{}.png".format(a, time.strftime('%Y%m%d_%H%M%S')))
                raise a
        else:
            try:
                text = self.login.get_the_text()
                self.assertIn(expected, text)
            except Exception as b:
                self.driver.get_screenshot_as_file("E:\\项目01\\TPshop\\screenshot\\{}_{}.png".format(b, time.strftime('%Y%m%d_%H%M%S')))
                raise b


if __name__ == '__main__':
    unittest.main()
