from selenium.webdriver.common.by import By
tpshop = "http://127.0.0.1"
"""首页"""
home_login = By.CSS_SELECTOR, '.red'#登录按钮
"""登录页"""
login_username = By.CSS_SELECTOR,'#username'#用户名
login_password = By.CSS_SELECTOR,'#password'#密码
login_code=By.CSS_SELECTOR,'#verify_code'#验证码
login_submit = By.CSS_SELECTOR,'.J-login-submit'#登录按钮
wrong_password = By.CSS_SELECTOR,'.layui-layer-content'#密码错误
