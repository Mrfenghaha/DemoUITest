# -*- coding: utf-8 -
import os
from selenium import webdriver as selenium_webdriver
from appium import webdriver as appium_webdriver
from selenium.webdriver.chrome.options import Options
from config.readConfig import *
from common.logger import Log
log = Log()

# 读取日志配置文件,定义所使用的记录器，getlogger()参数为空，则默认使用root级别的记录器
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class GetDriverWeb:
    def __init__(self, form):
        self.form = form

    def get_driver_web(self):
        if self.form == 'chrome':
            log.info('开始启动chrome浏览器')
            driver = selenium_webdriver.Chrome()
            # 将浏览器窗口最大化
            driver.maximize_window()
            driver.implicitly_wait(1)
            return driver
        elif self.form == 'h5':
            log.info('开始启动chrome浏览器-phone')
            mobile_emulation = {"deviceName": "iPhone 8"}
            chrome_options = Options()
            chrome_options.add_argument('disable-infobars')
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            driver = selenium_webdriver.Chrome(chrome_options=chrome_options)
            driver.implicitly_wait(1)
            return driver


class GetDriverAndroid:
    def __init__(self, android, reset):
        self.reset = reset  # 是否重启，目前支持'Reset'\'noReset'

    # 把启动android_app的功能封闭成方法
    def get_driver_android(self, reset):

        appFilePath = os.path.join(cur_path, 'app', app_info['appName'])
        start_info = {
            # 平台名称
            "platformName": 'Android',
            # 平台版本号
            "platformVersion": device_info['platformVersion'],
            # 设备名称
            'deviceName': device_info['deviceName'],
            # app文件地址
            'app': appFilePath,
            # app包名
            'appPackage': app_info['appPackage'],
            # app程序名
            'appActivity': app_info['appActivity'],
            # 是否不每次重新安装
            'noReset': reset,
            # 是否启用unicode键盘，启动可以输入中文
            'unicodeKeyboard': True,
            # 是否每次重新安装键盘
            'resetKeyboard': True,
            # 如果达到超时时间仍未接收到新的命令时appium会自动结束会话/秒
            'newCommandTimeout': 600}

        log.info('开始启动' + app_info['appName'])
        driver = appium_webdriver.Remote(appium_info['appiumIp'], start_info)
        return driver

    def get_driver_android_app(self):
        if self.reset == 'Reset':
            no_reset = False
        elif self.reset == 'noReset':
            no_reset = True

        driver = self.get_driver_android(no_reset)
        # 隐形等待,等待app加载完成
        driver.implicitly_wait(20)
        return driver
        

# 封装所有driver获取，因此命名为get_driver
def get_driver(form, *parm):

    if form == 'Chrome':
        driver = GetDriverWeb('chrome').get_driver_web()
        return driver
    elif form == 'H5':
        driver = GetDriverWeb('h5').get_driver_web()
        return driver
    elif form == 'Android':
        reset = parm[0]  # 是否重启，目前支持'Reset'\'noReset'
        driver = GetDriverAndroid(reset).get_driver_android_app()
        return driver
    else:
        print('参数错误请检查')


if __name__ == "__main__":
    get_driver('Chrome')
    get_driver('H5')
    get_driver('Android', 'Reset')
    get_driver('Android', 'noReset')
