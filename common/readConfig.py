# -*- coding: utf-8 -
import os
import yaml


# 人称最稳重方法，每加一层os.path.dirname()即向上翻一层,os.getcwd()获取当前目录的绝对路径
# os.getcwd()用于获取执行py文件的位置，例如在根目录执行获取的位置就是根目录，在common下执行就是common路径
# os.path.dirname(os.path.realpath(__file__))是获取包含该执行语句的py文件的绝对路径
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
config_path = os.path.join(cur_path, 'config')
env_file_path = os.path.join(config_path, 'env.yaml')
email_path = os.path.join(config_path, 'email.yaml')
app_file_path = os.path.join(config_path, 'deviceInfo.yaml')


# 如果没有config,自动创建
if not os.path.exists(app_file_path):
    os.mkdir(config_path)  # 创建config文件夹


# 如果没有config/deviceInfo.yaml,自动创建并写入默认值
if not os.path.exists(app_file_path):
    os.mknod(app_file_path)  # 创建env.yaml文件
    with open(app_file_path, 'w') as file:
        file.write('# 设备版本号\nplatformVersion: 6.0\n# 设备id\ndeviceName: 192.168.58.104:5555\n'
                   '# appium所在ip以及端口号\nappium_ip: http://127.0.0.1:4723/wd/hub')

with open(app_file_path, 'r', encoding='utf-8') as file:
    # 使用load方法将读出的字符串转字典;
    # 普通yaml.load(input)函数的PyYAML 5.1弃用
    app_data = yaml.full_load(file)
# 平台版本号
platformVersion = app_data['platformVersion']
# 设备名称
deviceName = app_data['deviceName']
# appium所在ip以及端口号
appium_ip = app_data['appium_ip']


# 如果没有config/env.yaml,自动创建并写入默认值
if not os.path.exists(env_file_path):
    os.mknod(env_file_path)  # 创建env.yaml文件
    with open(env_file_path, 'w') as file:
        file.write('# host环境IP\nhost: http://xxx.xx.x.xx\n'
                   '# mysql环境IP\nmysql_address: mysql+pymysql://qy:hello_qy@172.16.0.40:3306')

with open(env_file_path, 'r', encoding='utf-8') as file:
    # 使用load方法将读出的字符串转字典;
    # 普通yaml.load(input)函数的PyYAML 5.1弃用
    env_data = yaml.full_load(file)
# host地址
host = env_data['host']
# 数据库地址
mysql = env_data['mysql_address']


# 如果没有config/email.yaml,自动创建并写入默认值
if not os.path.exists(email_path):
    os.mknod(email_path)  # 创建email.yaml文件
    with open(email_path, 'w') as file:
        file.write("# 邮箱配置\n"
                   "server: xxx.xxx.xxx\n"
                   "sender: xxx@xxxxxx.com\n"
                   "password: xxxxxx\n"
                   "receiver: ['xxx@xxxxxx.com','xxx@xxxxxx.com']")


with open(email_path, 'r', encoding='utf-8') as file:
    # 使用load方法将读出的字符串转字典
    email_info = yaml.full_load(file)
# 邮箱服务器
email_server = email_info['server']
# 邮箱发送者
email_sender = email_info['sender']
# 邮箱密码
email_password = email_info['password']
# 邮箱接收者
email_receiver = email_info['receiver']

