# -*- coding: utf-8 -
import yaml
from common import *


class ReadConfigFile:
    def __init__(self, path):
        self.path = path

    def read_yaml_file(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            # 使用load方法将读出的字符串转字典
            content = yaml.full_load(file)
            file.close()
        return content


android_content = ReadConfigFile(android_path).read_yaml_file()
email_content = ReadConfigFile(email_yaml_path).read_yaml_file()
env_content = ReadConfigFile(env_yaml_path).read_yaml_file()


# 邮箱信息
email_info = email_content['email_info']


# APP信息
app_info = android_content['app_info']
# 设备信息
device_info = android_content['device_info']
# appium信息
appium_info = android_content['appium_info']


# host地址
host = env_content['host']
# mysql数据库信息
mysql_info = env_content['mysql_info']
# mongodb信息
mongodb_info = env_content['mongodb_info']
