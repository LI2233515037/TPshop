"""购物车页面"""
from base.base import BasePage, BaseHandle
from element import delete_selected_items, to_settle_accounts, keep_shopping, check_all


class PageShoppingTrolley(BasePage):
    def __init__(self):
        super().__init__()
        self.check_all = check_all  # 全选
        self.keep_shopping = keep_shopping  # 继续购物
        self.to_settle_accounts = to_settle_accounts  # 去结算
        self.delete_selected_items = delete_selected_items  # 删除选中的商品

    def page_check_all(self):
        return self.position_element(self.check_all)

    def page_keep_shopping(self):
        return self.position_element(self.keep_shopping)

    def page_to_settle_accounts(self):
        return self.position_element(self.to_settle_accounts)

    def page_delete_selected_items(self):
        return self.position_element(self.delete_selected_items)


class HandeleShoppingTrolley(BaseHandle):
    def __init__(self):
        self.handle_shopping_trolley = PageShoppingTrolley()

    def handle_check_all(self):
        pitch_on = self.handle_shopping_trolley.page_check_all()
        if not pitch_on.is_selected():
            self.base_click(pitch_on)

    def handle_keep_shopping(self):
        self.base_click(self.handle_shopping_trolley.page_keep_shopping())

    def handle_to_settle_accounts(self):
        self.base_click(self.handle_shopping_trolley.page_to_settle_accounts())

    def handle_delete_selected_items(self):
        self.base_click(self.handle_shopping_trolley.page_delete_selected_items())


class ProxyShoppingTrolley(object):
    def __init__(self):
        self.proxy_shopping_trolley = HandeleShoppingTrolley()

    def go_to_check_the_order_page(self):  # 跳转到结算页面
        self.proxy_shopping_trolley.handle_check_all()
        self.proxy_shopping_trolley.handle_to_settle_accounts()

    def proxy_delete_selected_items(self):  # 删除所有商品
        self.proxy_shopping_trolley.handle_check_all()
        self.proxy_shopping_trolley.handle_delete_selected_items()

    def go_to_home(self):  # 跳转到首页
        self.proxy_shopping_trolley.handle_keep_shopping()
