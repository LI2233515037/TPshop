import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
import logging.handlers


def log_log():
    # 初始化日志器
    log = logging.getLogger()
    # 初始化处理器
    log.setLevel(level=logging.INFO)
    # 控制台
    sh = logging.StreamHandler()

    # 文件
    th = logging.handlers.TimedRotatingFileHandler(
        filename=BASE_DIR + './info_{}.log'.format(time.strftime('%Y%m%d_%H%M%S')),
        when="S", interval=5, backupCount=4)
    # 初始化格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)

    # 添加格式器到处理器
    sh.setFormatter(formatter)
    th.setFormatter(formatter)
    # 添加处理器到日志器
    log.addHandler(sh)
    log.addHandler(th)
