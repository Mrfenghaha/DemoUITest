# -*- coding: utf-8 -
import os
import yaml


# 人称最稳重方法，每加一层os.path.dirname()即向上翻一层,os.getcwd()获取当前目录的绝对路径
# os.getcwd()用于获取执行py文件的位置，例如在根目录执行获取的位置就是根目录，在common下执行就是common路径
# os.path.dirname(os.path.realpath(__file__))是获取包含该执行语句的py文件的绝对路径
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
config_path = os.path.join(cur_path, 'config')
env_info_path = os.path.join(config_path, 'env.yaml')
email_info_path = os.path.join(config_path, 'email.yaml')
android_info_path = os.path.join(config_path, 'android.yaml')


# 如果没有config/email.yaml,自动创建并写入默认值
if not os.path.exists(email_info_path):
    with open(email_info_path, mode='a', encoding='utf-8') as f:
        pass  # 创建email.yaml文件,支持mac osx创建文件
    # os.mknod(email_info_path)  # 创建email.yaml文件
    with open(email_info_path, 'w', encoding='utf-8') as file:
        file.write("# 邮箱配置\n"
                   "server: xxx.xxx.xxx\n"
                   "sender: xxx@xxxxxx.com\n"
                   "password: xxxxxx\n"
                   "receiver: ['xxx@xxxxxx.com','xxx@xxxxxx.com']")
    file.close()


with open(email_info_path, 'r', encoding='utf-8') as file:
    # 使用load方法将读出的字符串转字典
    # 普通yaml.load(input)函数的PyYAML 5.1弃用
    email_info = yaml.full_load(file)
    file.close()
# 邮箱服务器
email_server = email_info['server']
# 邮箱发送者
email_sender = email_info['sender']
# 邮箱密码
email_password = email_info['password']
# 邮箱接收者
email_receiver = email_info['receiver']


# 如果没有config/android.yaml,自动创建并写入默认值
if not os.path.exists(android_info_path):
    with open(android_info_path, mode='a', encoding='utf-8') as f:
        pass  # 创建android.yaml文件,支持mac osx创建文件
    # os.mknod(android_info_path)  # 创建android.yaml文件
    with open(android_info_path, 'w', encoding='utf-8') as file:
        file.write('# APP名称\nappName: xxx\n# APP包名\nappPackage: xxx\n# APP程序名\nappActivity: xxx\n'
                   '# 设备版本号\nplatformVersion: 6.0\n# 设备id\ndeviceName: 192.168.58.104:5555\n'
                   '# appium所在ip以及端口号\nappiumIp: http://127.0.0.1:4723/wd/hub\n')
    file.close()

with open(android_info_path, 'r', encoding='utf-8') as file:
    # 使用load方法将读出的字符串转字典;
    # 普通yaml.load(input)函数的PyYAML 5.1弃用
    android_info = yaml.full_load(file)
    file.close()
# 平台版本号
platformVersion = android_info['platformVersion']
# 设备名称
deviceName = android_info['deviceName']
# appium所在ip以及端口号
appium_ip = android_info['appiumIp']


# 如果没有config/env.yaml,自动创建并写入默认值
if not os.path.exists(env_info_path):
    with open(env_info_path, mode='a',encoding='utf-8') as f:
        pass  # 创建env.yaml文件,支持mac osx创建文件
    # os.mknod(env_info_path)  # 创建env.yaml文件
    with open(env_info_path, 'w') as file:
        file.write('# host环境IP\nhost: http://xxx.xx.x.xx\n'
                   '# mysql服务信息\nmysql_ip: xxxx\n'
                   'mysql_port: 3306\n'
                   'mysql_account: xxxx\n'
                   'mysql_password: xxxx\n')

with open(env_info_path, 'r', encoding='utf-8') as file:
    # 使用load方法将读出的字符串转字典;
    # 普通yaml.load(input)函数的PyYAML 5.1弃用
    env_info = yaml.full_load(file)
# host地址
host = env_info['host']
# 数据库IP
mysql_ip = env_info['mysql_ip']
# 数据库端口号
mysql_port = env_info['mysql_port']
# 数据库账号
mysql_account = env_info['mysql_account']
# 数据库密码
mysql_password = env_info['mysql_password']
