# 框架介绍
本框架使用Selenium、Appium工具，采用PO设计模式，实现Web、Android的UI自动化测试。（可一个用例中同时启动web、android）

由于考虑不同项目的情况，为保持灵活性，本框架对于用例编写部分并未进行更多的封装，使用本框架仍需要一些Python编码基础


# 环境/使用介绍
## 环境说明
* 安装python3环境
* 安装相关模块库
```
pip3 install -r requirements.txt
```
* 下载chromedriver驱动(注意下载对应版本的驱动)，并放置指定位置
```
驱动下载地址1：http://npm.taobao.org/mirrors/chromedriver/
驱动下载地址2：http://chromedriver.storage.googleapis.com/index.html

ubuntu
sudo mv chromedriver /usr/bin/chromedriver

mac
sudo mv chromedriver /usr/local/bin

windows放在python安装路径的Scripts/文件下
C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts
```
* 安装并开启Appium服务（appium server或启动程序均可）
```
客户端下载地址：https://github.com/appium/appium-desktop/releases/tag/v1.15.1
```
## 配置说明
1. 邮件发送
    * config/email.yaml文件,用于测试报告邮件发送，需要配置邮箱相关信息
2. 配置env环境参数
    * config/env.yaml文件,用于数据库连接、host设置
    * envDev.yaml/envSt.yaml分别为对应环境的配置信息
    * 可以添加更多环境，直接添加相应的envXx.yaml文件即可，运行用例时使用Xx作为环境参数即可 
    * 当需要多环境执行时，env.yaml文件变为数据传输中介不再需要维护

## 功能用例执行说明
runcase.py脚本为功能测试用例执行统一入口

**查看帮助--help**
```
python3 runcase.py --help
usage: runcase.py [-h] [--env ENV] --suite SUITE --name NAME

optional arguments:
  -h, --help            show this help message and exit
  --env ENV, -e ENV     环境变量参数，非必要参数
  --suite SUITE, -s SUITE
                        测试用例集名称(tests/testcase/目录下文件名)，必要参数
  --name NAME, -n NAME  测试用例名称，必要参数
```

**执行用例**

```
python3 runcase.py -n $env -s $suite -n $name  # 在$env环境下,执行用例,$suite文件夹路径,$name文件名称或all(all即可该用例集下左右用例)
例：
python3 runcase.py -s api_test -n test_login
python3 runcase.py -s api_test -n all
python3 runcase.py -s api_test -n all
```

# 框架详细介绍

![](https://github.com/fengyibo963/DemoUITest/blob/master/docs/%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84.png)

## 用例分层概念介绍
该框架分层使用PO设计模式，BDD理念

* Page（页面）：封装页面为类，并且封装所有操作
* Suite（动作）：封装动作(行为)（动作：例如登录动作，需要填写账号、填写密码、点击登录按钮）
* TestCase（用例）：使用动作(行为)拼接工作流，并且对于所有动作可以进行断言

由于某些操作自身就可以定义为动作，因为TestCase既可以使用Suite拼接，也可以使用Page进行拼接（或混合拼接）。

如果为了更好的理解分层，同时增强TestCase脚本的可读性，可以封装所有动作仅使用Suite拼接TestCase（单同时代码量、维护成本会相应的增高）

TestCase拼接为简单关键字驱动模式，使用动作的函数名或类型作为关键字，并且Python语言自身按照顺序执行的机制，达到直接拼接的效果

## 简单数据驱动介绍
对于所有输入参数均进行高度参数化，将需要的所有参数进行参数化，这样使得操作代码的复用性、维护性提高

所有对于不同的测试场景，仅直接通过不同的测试数据组合实现

## 数据库操作介绍
由于一些原因可能需要断言的数据并不能从页面中获取仅仅记录在数据库，或者需要清理自动化测试产生的系统数据等，造成需要添加数据库操作拓展

## 数据生成器介绍
接口需要的参数有一些并不能固定设置，例如时间戳、UUID等不可重复参数，或者因为业务需要不能重复的手机号等等参数。

为了做到真正的自动化扩展使用数据生成器，使用生成器按照规则生成想要的数据字典，在编写TestCase的使用直接调用生成器并提取参数即可

## 编写规范介绍
为了代码的可读性，指定了一些编写[规范](https://github.com/fengyibo963/DemoUITest/blob/master/docs/%E7%BC%96%E5%86%99%E8%AF%B4%E6%98%8E.md)说明（可根据自己喜好修改）

## 项目结构详细介绍

![](https://github.com/fengyibo963/DemoUITest/blob/master/docs/%E9%A1%B9%E7%9B%AE%E7%9B%AE%E5%BD%95.png)

```
|-- common      # 基础通用方法，使用过程中基本无需修改（可以二次开发自行拓展）
|    -- __init__.py  # 所有需要自动创建的文件和默认文件
|    -- baseView.py  # 定义driver方法，将所有基础方法重定义(一是为了统计所有使用到的基础方法便于其他人学习;二是为了简化项目编码维护)
|    -- dataType.py  # 字符格式转换,同一封装使用
|    -- emailSend.py  # 测试执行后的邮件发送配置(收件人配置)
|    -- envSpecify.py  # env环境切换方法
|    -- HTMLTestRunner.py  # unittest测试执行生成测试报告的报告文件
|    -- logger.py  # 功能测试log输出配置
|    -- readConfig.py  # 读取环境变量
|    -- getDriver.py  # 启动浏览器、APP获取driver
|-- config
|    -- email.yaml  # 邮件发送邮箱配置
|    -- env.yaml  # 环境变量
|    -- envDev.yaml  # 开发环境配置文件，可以根据自己需要添加删除
|    -- envSt.yaml  # 测试环境配置文件，可以根据自己需要添加删除
|-- data
|    -- dataCreate  # 测试数据生成
|        -- xxxx.py  # 某些特殊数据的生成
|    -- dbOperation  # 数据库数据操作  
|        -- xxxx.py  # 某些数据库操作的封装
|    -- data_create.py  # 某产品线测试数据生成
|    -- db_operation.py  # 数据库方法的统一调用入口
|-- docs
|-- result
|    -- logs   # 生成的log文件存储位置
|    -- logsLocust   # 生成的Locust的log文件存储位置
|    -- reports     # 生成的测试报告存储位置
|-- tests
|    -- pages
|        -- xxxxxxx  # 某产品(app或web)
|            -- page_xxxx.py  # 该产品某一页面
|    -- suitess
|        -- xxxxxxx  # 某产品(app或web)
|            --suite_xxxx.py  # 该产品通用封装的模块
|    -- testcases
|        -- func_xxxxxxx  # 某产品线功能逻辑测试用例
|        -- page_xxxxxxx  # 某产品线页面测试用例
|        -- smokec_xxxxxxx  # 某产品线冒烟测试用例
|            -- test_xxx.py  # 测试用例文件
|-- runcase.py     # 通过参数执行任一测试用例或测试用例集
|-- requirements.txt    # 该文件记录所有需要用的框架（以便更换环境一键安装）
```

## 相关库介绍
* 该框架使用Selenium、Appium库作为UI操作的基础库
* 使用Unittest作为用例集、用例执行调度
* 使用Pymysql连接操作Mysql数据库
* 使用pymongo连接操作MongoDB数据库
* 使用Yaml文件作为配置文件格式