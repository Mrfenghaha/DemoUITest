# -*- coding: utf-8 -
import os

cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
result_path = os.path.join(cur_path, "result")
logs_path = os.path.join(result_path, 'logs')
reports_path = os.path.join(result_path, "reports")

# 如果不存在这个result文件夹，就创建一个
if not os.path.exists(result_path):
    os.mkdir(result_path)
# 如果没有result/logs文件夹，就创建一个
if not os.path.exists(logs_path):
    os.mkdir(logs_path)
# 如果没有result/reports文件夹，就创建一个
if not os.path.exists(reports_path):
    os.mkdir(reports_path)

config_path = os.path.join(cur_path, 'config')
env_yaml_path = os.path.join(config_path, 'env.yaml')
email_yaml_path = os.path.join(config_path, 'email.yaml')
android_path = os.path.join(config_path, 'android.yaml')

# 如果没有config文件夹，就创建一个
if not os.path.exists(config_path):
    os.mkdir(config_path)  # 创建config文件夹

# 如果没有config/email.yaml,自动创建并写入默认值
if not os.path.exists(email_yaml_path):
    with open(email_yaml_path, 'w', encoding='utf-8') as file:
        file.write("# 邮箱配置\nemail_info:\n"
                   "  server: xxx.xxx.xxx\n"
                   "  sender: xxx@xxxxxx.com\n"
                   "  password: xxxxxx\n"
                   "  receiver: ['xxx@xxxxxx.com','xxx@xxxxxx.com']")
    file.close()


# 如果没有config/env.yaml,自动创建并写入默认值
if not os.path.exists(env_yaml_path):
    with open(env_yaml_path, 'w', encoding='utf-8') as file:
        file.write('# host环境IP\nhost: http://xxx.xx.x.xx\n'
                   '# mysql服务信息\nmysql_info:\n  ip:xxxx\n  port: 3306\n  account: xxxx\n  password: xxxx\n'
                   '# mongodb服务信息\nmongodb_info:\n  ip:xxxx\n  port: 3306\n  account: xxxx\n  password: xxxx\n')
    file.close()


if not os.path.exists(android_path):
    with open(android_path, 'w', encoding='utf-8') as file:
        file.write('app_info:\n'
                   '  # APP名称\n  appName: xxx\n'
                   '  # APP包名\n  appPackage: xxx\n'
                   '  # APP程序名\n  appActivity: xxx\n'
                   'device_info:\n'
                   '  # 设备版本号\n  platformVersion: 6.0\n'
                   '  # 设备id\n  deviceName: 192.168.58.104:5555\n'
                   'appium_info:\n'
                   '  #appium所在ip以及端口号\n  appiumIp: http://127.0.0.1:4723/wd/hub\n')
    file.close()
