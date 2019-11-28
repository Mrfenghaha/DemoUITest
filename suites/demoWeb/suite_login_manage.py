# -*- coding: utf-8 -
from time import sleep
from common.readConfig import *
from common.baseView import Common
from pages.demoWeb.page_login import LoginDefault


def login_manage(driver, data):
    # 打开web端网页
    Common(driver).get(phl_manage)
    # 管理端登录(进入新页面,等待1s)
    phone = data['manage_email']
    password = data['manage_password']
    LoginDefault(driver).management_login(phone, password)
    sleep(1)
