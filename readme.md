# 介绍
本框架使用python3+selenium+appium+unittest、PO模式，实现Web、Android的UI自动化测试。
可实现同一用例同时启动web、android

# 文档
* docs文件夹中有关于编写说明、项目结构、项目结构详细介绍的文档，请详细查看

# 环境准备
* 首先需要安装python3.x环境（linux系列不需要安装）
* 下载chromedriver驱动(注意下载对应版本的驱动)，并放置指定位置（不同系统放置位置不同，请自行百度）
```
驱动下载地址1：http://npm.taobao.org/mirrors/chromedriver/
驱动下载地址2：http://chromedriver.storage.googleapis.com/index.html
```
* 安装并开启Appium服务（appium server或启动程序均可）
```
客户端下载地址：https://github.com/appium/appium-desktop/releases/tag/v1.15.1
```
* 安装模块库
```
pip3 install -r requirements.txt
```

## 编辑配置文件
### 配置邮件发送
* 编辑config/email.yaml文件,用于测试报告邮件发送
### 配置Android、APP连接
* 编辑config/android.yaml文件,用于app连接
### 配置env环境参数
* 编辑config/env/envDev.yaml文件,用于开发环境数据库连接、host设置
* 编辑config/env/envSt.yaml文件,用于测试环境数据库连接、host设置
* 可以添加更多环境，直接添加相应的envXx.yaml文件即可，运行用例是使用Xx作为参数即可 

# 用例执行说明
```
python3 runcase.py $env $suite $name  # 在$env环境下，执行用例,$suite文件夹路径,$name文件名称或all
例：
python3 runcase.py Dev testcase/demo test_first  # 在开发环境下，执行testcase/demo/test_first用例
python3 runcase.py St testcase/demo all  # 在测试环境下，执行testcase/demo文件夹下的所有用例
```
