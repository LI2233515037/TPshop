import os
import time

from selenium.webdriver.support.wait import WebDriverWait

from element import wrong_password, successfully_added
from utlist import BrowserDriven
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class BasePage(object):
    def __init__(self):
        self.driver = BrowserDriven.get_driver()

    def position_element(self, loc, timeout=30, poll=0.5):  # 元素定位
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))


class BaseHandle(object):  # 点击元素
    def base_click(self, element):
        element.click()

    def base_import(self, element, value):  # 输入文本
        text = element
        text.clear()
        text.send_keys(value)

    def base_text(self):  # 获取文本元素
        pass


def popover_content():
    text = BrowserDriven.get_driver().find_elements_by_css_selector(".layui-layer-ico2").text
    print(text)


def switching_forms(text):
    driver = BrowserDriven.get_driver()
    driver.switch_to.frame(driver.find_element_by_tag_name(text))

def Image_save_path(text):
    driver = BrowserDriven.get_driver()
    driver.get_screenshot_as_file(BASE_DIR + "\\screenshot\\{}_{}.png".format(text, time.strftime('%Y%m%d_%H%M%S')))

def switch_of_windows():#窗口切换
    driver = BrowserDriven.get_driver()
    handle = driver.window_handles
    driver.switch_to.window(handle[-1])
