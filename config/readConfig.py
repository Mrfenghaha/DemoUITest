# -*- coding: utf-8 -
import os
import yaml


# 人称最稳重方法，每加一层os.path.dirname()即向上翻一层,os.getcwd()获取当前目录的绝对路径
# os.getcwd()用于获取执行py文件的位置，例如在根目录执行获取的位置就是根目录，在common下执行就是common路径
# os.path.dirname(os.path.realpath(__file__))是获取包含该执行语句的py文件的绝对路径
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
config_path = os.path.join(cur_path, 'config')

env_path = os.path.join(config_path, 'env.yaml')
email_path = os.path.join(config_path, 'email.yaml')
android_path = os.path.join(config_path, 'android.yaml')


# 如果没有config/email.yaml,自动创建并写入默认值
if not os.path.exists(email_path):
    with open(email_path, 'w', encoding='utf-8') as file:
        file.write("# 邮箱配置\nemail_info:\n"
                   "  server: xxx.xxx.xxx\n"
                   "  sender: xxx@xxxxxx.com\n"
                   "  password: xxxxxx\n"
                   "  receiver: ['xxx@xxxxxx.com','xxx@xxxxxx.com']")
    file.close()


with open(email_path, 'r', encoding='utf-8') as file:
    # 使用load方法将读出的字符串转字典
    # 普通yaml.load(input)函数的PyYAML 5.1弃用
    email = yaml.full_load(file)
    file.close()
# 邮箱信息
email_info = email['email_info']


# 如果没有config/android.yaml,自动创建并写入默认值
if not os.path.exists(android_path):
    with open(android_path, 'w', encoding='utf-8') as file:
        file.write('# APP名称\nappName: xxx\n# APP包名\nappPackage: xxx\n# APP程序名\nappActivity: xxx\n'
                   '# 设备版本号\nplatformVersion: 6.0\n# 设备id\ndeviceName: 192.168.58.104:5555\n'
                   '# appium所在ip以及端口号\nappiumIp: http://127.0.0.1:4723/wd/hub\n')
    file.close()

with open(android_path, 'r', encoding='utf-8') as file:
    # 使用load方法将读出的字符串转字典;
    # 普通yaml.load(input)函数的PyYAML 5.1弃用
    android = yaml.full_load(file)
    file.close()
# APP信息
app_info = android['app_info']
# 设备信息
device_info = android['device_info']
# appium信息
appium_info = android['appium_info']


# 如果没有config/env.yaml,自动创建并写入默认值
if not os.path.exists(env_path):
    with open(env_path, 'w') as file:
        file.write('# host环境IP\nhost: http://xxx.xx.x.xx\n'
                   '# mysql服务信息\nmysql_ip: xxxx\n'
                   'mysql_port: 3306\n'
                   'mysql_account: xxxx\n'
                   'mysql_password: xxxx\n')

with open(env_path, 'r', encoding='utf-8') as file:
    # 使用load方法将读出的字符串转字典;
    # 普通yaml.load(input)函数的PyYAML 5.1弃用
    env = yaml.full_load(file)
# host地址
host = env['host']
# mysql数据库信息
mysql_info = env['mysql_info']
# mongodb信息
mongodb_info = env['mongodb_info']
