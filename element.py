from selenium.webdriver.common.by import By

tpshop = "http://127.0.0.1"
"""加入购物弹窗"""
successfully_added = 'iframe'  # 成功加入购物车弹窗
successfully_added_text = By.CSS_SELECTOR, '.conect-title'  # 添加成功
Keep_shopping = By.CSS_SELECTOR, '.go-shopping'  # 继续购物
shopping_cart_settlement = By.CSS_SELECTOR, 'ui-button-122'  # 去购物车结算
"""首页"""
home_login = By.CSS_SELECTOR, '.red'  # 登录按钮
input_box = By.CSS_SELECTOR, '#q'  # 输入框
search_button = By.CSS_SELECTOR, '.ecsc-search-button'  # 搜索按钮
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
