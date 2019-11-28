# -*- coding: utf-8 -
import os
from selenium import webdriver as selenium_webdriver
from appium import webdriver as appium_webdriver
from selenium.webdriver.chrome.options import Options
from common.readConfig import *
from common.logger import Log
from common.baseView import Common
from selenium.webdriver.common.by import By
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
        self.android = android  # app名称，目前支持'Peso2Go'\'MQuickRupee'
        self.reset = reset  # 是否重启，目前支持'Reset'\'noReset'

    # 把启动android_app的功能封闭成方法
    def get_driver_android(self, app_name, app_package, app_activity, reset):

        app_path = os.path.join(cur_path, 'app', app_name)
        start_info = {
            # 平台名称
            "platformName": 'Android',
            # 平台版本号
            "platformVersion": platformVersion,
            # 设备名称
            'deviceName': deviceName,
            # app文件地址
            'app': app_path,
            # app包名
            'appPackage': app_package,
            # app程序名
            'appActivity': app_activity,
            # 是否不每次重新安装
            'noReset': reset,
            # 是否启用unicode键盘，启动可以输入中文
            'unicodeKeyboard': True,
            # 是否每次重新安装键盘
            'resetKeyboard': True,
            # 如果达到超时时间仍未接收到新的命令时appium会自动结束会话/秒
            'newCommandTimeout': 600}

        log.info('开始启动' + app_name)
        driver = appium_webdriver.Remote(appium_ip, start_info)
        return driver

    def get_driver_android_app(self):
        if self.reset == 'Reset':
            no_reset = False
        elif self.reset == 'noReset':
            no_reset = True

        if self.android == 'Peso2Go':
            app_name = 'Peso2Go.apk'
            app_package = 'com.demoApp'
            app_activity = 'com.demoApp.MainActivity'

            driver = self.get_driver_android(app_name, app_package, app_activity, no_reset)
            # 隐形等待,等待app加载完成
            driver.implicitly_wait(20)
            # 根据是否重新安装判断是否需要检查权限
            if self.reset == 'Reset':
                Common(driver).check_device_gps_btn()
            elif self.reset == 'noReset':
                pass
            return driver
        elif self.android == 'MQuickRupee':
            app_name = 'MQuickRupee.apk'
            app_package = 'com.MQuickRupee'
            app_activity = 'com.MQuickRupee.MainActivity'

            driver = self.get_driver_android(app_name, app_package, app_activity, no_reset)
            # 隐形等待,等待app加载完成
            driver.implicitly_wait(20)
            # 根据是否重新安装判断是否需要检查权限
            if self.reset == 'Reset':
                ok_type = (By.ID, 'btn-submit')
                start_type = (By.ID, 'btn-guide-start')
                common = Common(driver)
                # 点击i_know按钮
                common.find_element(*ok_type).click()
                # 授权
                common.check_device_permissions()
                # 左滑动2次屏幕
                common.device_screen_swipe('left', 3)
                # 点击getting started按钮
                common.find_element(*start_type).click()
                log.info('MQuickRupee,引导页面,getting started按钮')
            elif self.reset == 'noReset':
                pass
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
        android = parm[0]  # app名称，目前支持'Peso2Go'\'MQuickRupee'
        reset = parm[1]  # 是否重启，目前支持'Reset'\'noReset'
        driver = GetDriverAndroid(android, reset).get_driver_android_app()
        return driver
    else:
        print('参数错误请检查')


if __name__ == "__main__":
    get_driver('Chrome')
    get_driver('H5')
    get_driver('Android', 'Peso2Go', 'Reset')
    get_driver('Android', 'MQuickRupee', 'Reset')
