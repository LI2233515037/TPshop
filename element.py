from selenium.webdriver.common.by import By

tpshop = "http://127.0.0.1"
"""加入购物弹窗"""
successfully_added = '#layui-layer-iframe1'  # 成功加入购物车弹窗
successfully_added_text = By.CSS_SELECTOR, '.conect-title'  # 添加成功
Keep_shopping = By.CSS_SELECTOR, '.go-shopping'  # 继续购物
shopping_cart_settlement = By.CSS_SELECTOR, 'ui-button-122'  # 去购物车结算
"""首页"""
home_login = By.CSS_SELECTOR, '.red'  # 登录按钮
input_box = By.CSS_SELECTOR, '#q'  # 输入框
search_button = By.CSS_SELECTOR, '.ecsc-search-button'  # 搜索按钮
shopping_trolley = By.CSS_SELECTOR, '.share-shopcar-index'  # 购物车
my_order = By.XPATH, '//*[contains(text(),"{}")]'  # 我的订单
product_categories = By.CSS_SELECTOR, '[title="{}"]'  # 全部商品分类
"""登录页"""
login_username = By.CSS_SELECTOR, '#username'  # 用户名
login_password = By.CSS_SELECTOR, '#password'  # 密码
login_code = By.CSS_SELECTOR, '#verify_code'  # 验证码
login_submit = By.CSS_SELECTOR, '.J-login-submit'  # 登录按钮
wrong_password = By.CSS_SELECTOR, '.layui-layer-content'  # 密码错误
"""商品列表页"""
commodity = By.XPATH, "//*[@class='shop_name2']/*[contains(text(),'{}')]"  # 商品
"""商品详情页"""
add_to_shopping_cart = By.CSS_SELECTOR, '#join_cart'  # 加入购物车
buy_it_now_price = By.CSS_SELECTOR, '#join_cart_now'  # 立即购买
"""购物车页面"""
check_all = By.CSS_SELECTOR, '.checkall'  # 全选
keep_shopping = By.CSS_SELECTOR, '.gwc-jxgw'  # 继续购物
to_settle_accounts = By.CSS_SELECTOR, '.paytotal'  # 去结算
delete_selected_items = By.CSS_SELECTOR, '#removeGoods'  # 删除选中商品
"""核对订单页面"""
submit_order = By.CSS_SELECTOR, '#submit_order'  # 提交订单
order_submitted_successfully = By.CSS_SELECTOR, '.erhuh'  # 订单提交成功
"""成功提交订单页面"""
pay_on_delivery = By.CSS_SELECTOR, '[value="pay_code=cod"]'  # 货到付款
Confirm_payment_method = By.CSS_SELECTOR, '.button-confirm-payment'  # 确认支付方式
order_payment_success = By.CSS_SELECTOR, '.erhuh'  # 订单支付成功文案

"""个人中心"""
obligation = By.LINK_TEXT, '{}'  # 待付款
immediate_payment = By.CSS_SELECTOR, '.ps_lj'  # 立即支付
Query_box = By.CSS_SELECTOR, '#submit_order'  # 搜索框
inquire = By.CSS_SELECTOR, '#submit_order'  # 查询

cookis = [{'domain': '127.0.0.1', 'httpOnly': False, 'name': 'parent_region', 'path': '/', 'secure': False,
           'value': '%5B%7B%22id%22%3A3%2C%22name%22%3A%22%u4E1C%u57CE%u533A%22%7D%2C%7B%22id%22%3A14%2C%22name%22%3A%22%u897F%u57CE%u533A%22%7D%2C%7B%22id%22%3A22%2C%22name%22%3A%22%u5D07%u6587%u533A%22%7D%2C%7B%22id%22%3A30%2C%22name%22%3A%22%u5BA3%u6B66%u533A%22%7D%2C%7B%22id%22%3A39%2C%22name%22%3A%22%u671D%u9633%u533A%22%7D%2C%7B%22id%22%3A83%2C%22name%22%3A%22%u4E30%u53F0%u533A%22%7D%2C%7B%22id%22%3A105%2C%22name%22%3A%22%u77F3%u666F%u5C71%u533A%22%7D%2C%7B%22id%22%3A115%2C%22name%22%3A%22%u6D77%u6DC0%u533A%22%7D%2C%7B%22id%22%3A145%2C%22name%22%3A%22%u95E8%u5934%u6C9F%u533A%22%7D%2C%7B%22id%22%3A159%2C%22name%22%3A%22%u623F%u5C71%u533A%22%7D%2C%7B%22id%22%3A188%2C%22name%22%3A%22%u901A%u5DDE%u533A%22%7D%2C%7B%22id%22%3A204%2C%22name%22%3A%22%u987A%u4E49%u533A%22%7D%2C%7B%22id%22%3A227%2C%22name%22%3A%22%u660C%u5E73%u533A%22%7D%2C%7B%22id%22%3A245%2C%22name%22%3A%22%u5927%u5174%u533A%22%7D%2C%7B%22id%22%3A264%2C%22name%22%3A%22%u6000%u67D4%u533A%22%7D%2C%7B%22id%22%3A281%2C%22name%22%3A%22%u5E73%u8C37%u533A%22%7D%5D'},
          {'domain': '127.0.0.1', 'expiry': 1681547176, 'httpOnly': False, 'name': 'district_id', 'path': '/',
           'secure': False, 'value': '3'},
          {'domain': '127.0.0.1', 'expiry': 1681547176, 'httpOnly': False, 'name': 'province_id', 'path': '/',
           'secure': False, 'value': '1'},
          {'domain': '127.0.0.1', 'httpOnly': False, 'name': 'is_distribut', 'path': '/', 'secure': False,
           'value': '0'},
          {'domain': '127.0.0.1', 'expiry': 1681547176, 'httpOnly': False, 'name': 'city_id', 'path': '/',
           'secure': False, 'value': '2'},
          {'domain': '127.0.0.1', 'httpOnly': False, 'name': 'uname', 'path': '/', 'secure': False, 'value': 'summer'},
          {'domain': '127.0.0.1', 'httpOnly': False, 'name': 'user_id', 'path': '/', 'secure': False, 'value': '8'},
          {'domain': '127.0.0.1', 'httpOnly': False, 'name': 'cn', 'path': '/', 'secure': False, 'value': '0'},
          {'domain': '127.0.0.1', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False,
           'value': 'fkl9gogvam2imgl35r90j8gj71'},
          {'domain': '127.0.0.1', 'expiry': 1678958778, 'httpOnly': False, 'name': 'is_mobile', 'path': '/',
           'secure': False, 'value': '0'},
          {'domain': '127.0.0.1', 'expiry': 1679041537, 'httpOnly': False, 'name': 'CNZZDATA009', 'path': '/',
           'secure': False, 'value': '30037667-1536735'}]
