import time
import unittest

from selenium import webdriver

from element import tpshop


class BrowserDriven():
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.get(tpshop)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None

if __name__ == '__main__':
    BrowserDriven.get_driver()
    time.sleep(10)
    BrowserDriven.quit_driver()