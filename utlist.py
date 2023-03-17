import time

from selenium import webdriver

from element import tpshop, cookis


class BrowserDriven(object):
    driver = None
    exit_status = True

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.get(tpshop)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(5)
            cls.driver.delete_all_cookies()
            for cookies in cookis:
                cls.driver.add_cookie(cookies)
            cls.driver.refresh()
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver and cls.exit_status:
            cls.driver.quit()
            cls.driver = None

    @classmethod
    def driver_exit_status(cls, status):
        cls.exit_status = status


if __name__ == '__main__':
    driver = BrowserDriven.get_driver()
    # driver.delete_all_cookies()
    # time.sleep(100)
    # print(driver.get_cookies())
    time.sleep(5)
    BrowserDriven.quit_driver()
