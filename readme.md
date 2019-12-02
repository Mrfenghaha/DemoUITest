# 介绍
本框架使用python3+selenium+appium+unittest、PO模式，实现Web、Android的UI自动化测试。
可实现同一用例同时启动web、android

# 文档
* docs文件夹中有关于编写说明、项目结构、项目结构详细介绍的文档，请详细查看

# 环境准备
* 首先需要安装python3.x环境（linux系列不需要安装）
* 下载Chrome镜像放置指定位置
* 安装并开启Appium服务（appium server或启动程序均可）
* 安装模块库
```
pip3 install -r requirements.txt
```

## 编辑配置文件
* 编辑config/email.yaml文件,用于测试报告邮件发送
* 编辑config/env.yaml文件,用于数据库连接、host设置
* 编辑config/android.yaml文件,用于app连接

# 用例执行说明
```
python3 runcase.py $suite $name  # 执行用例,$suite文件夹路径,$name文件名称或all
例：
python3 runcase.py testcase/demo test_first  # 执行testcase/demo/test_first用例
python3 runcase.py testcase/demo all  # 执行testcase/demo文件夹下的所有用例
```
