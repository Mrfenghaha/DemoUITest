# 项目结构详细讲解
```
xxxx(项目名称)
|-- app
|    -- xxx.apk   # app包文件
|-- common      # 相同基础通用方法
|    -- baseView.py  # 定义driver方法，将所有基础方法重定义(一是为了统计所有使用到的基础方法便于其他人学习;二是为了简化项目编码维护)
|    -- dataType.py  # 字符格式转换,同一封装使用
|    -- emailSend.py  # 测试执行后的邮件发送配置(收件人配置)
|    -- HTMLTestRunner.py  # unittest测试执行生成测试报告的报告文件
|    -- logger.py  # log输出配置
|    -- readConfig.py  # 读取环境变量\设备信息
|    -- start_browser.py  # 启动浏览
|    -- start_xxxxx.py  # 启动指定app
|-- config
|    -- deviceInfo.py  # 移动设备信息
|    -- env.py  # 环境变量
|-- data
|    -- data_create  # 测试数据生成
|        -- xx_data_create  # 某产品线测试数据生成
|    -- mysql  # 数据库数据操作     
|-- docs
|-- logs   # 生成的log文件存储位置
|-- reports     # 生成的测试报告存储位置
|-- pages
|    -- xxxxxxx  # 某产品(app或web)
|        -- page_xxxx.py  # 该产品某一页面
|-- suitess
|    -- xxxxxxx  # 某产品(app或web)
|        --suite_xxxx.py  # 该产品通用封装的模块
|-- testcases
|    -- func_xxxxxxx  # 某产品线功能逻辑测试用例
|    -- page_xxxxxxx  # 某产品线页面测试用例
|    -- smokec_xxxxxxx  # 某产品线冒烟测试用例
|        -- test_xxx.py  # 测试用例文件
|-- run_case.py     # 通过参数执行任一测试用例或测试用例集
|-- requirements.txt    # 该文件记录所有需要用的框架（以便更换环境一键安装）
```

# 元素定位
* 统一使用id进行定位
* 对于前端无法设置id的元素,才考虑使用其他方式定位(首推荐XPATH)
* 由于部分元素,前端设置id(只能设置于其上一层位置),使用XPATH进行定位
* 元素定位,统一使用xxx_type命名

# 元素操作
* 目前使用到的元素操作,以输入框填写(send)/按钮点击(click)/鼠标移动(set)/获取元素文字(get),四种为主
* 输入框填写  函数名统一使用send_xx_xx_action()
* 按钮点击    函数名统一使用click_xx_xx_action()
* 鼠标移动    函数名统一使用set_xx_xx_action()
* 获取元素文字  函数名统一使用get_xx_xx_action()

# 页面class
* 每一个页面为一个class,一个文件(同一页面不同用途,视为同一页面.例:详情页,编辑/查看等)  统一使用XXXPage对class命名
* 对于大多数页面均出现的元素,单独class   统一使用XXX对class命名
* 对于web或app使用的插件,统一单独class  统一使用PlugIn对class命名
* 对于web或app某一页面,有常用操作的   统一使用XXXDefault对class命名

# 文件命名
* 对于页面文件,命名page_xx.py
* 对于模块文件,命名suite_xx.py
* 对于测试用例文件,命名test_xx.py

# 测试用例函数命名
* 测试用例函数命名统一使用test_case01格式命名

# 元素操作错误重试(app)
* 对于点击后需要展开弹窗\相机\日历等等插件\设备原生程序的操作,添加错误重试(必添加)
* 对于点击后进入新页面的操作,添加错误重试(根据实际情况)

# 操作等待
* 由于目前前端app是整页加载,没有使用ajax的模块化加载;所以,整体使用隐形等待,不需要添加sleep强制等待
* 对于需要数据库操作时,元素操作完要添加sleep强制等待(因为前端操作到后端处理完毕有时间差)
* web加载较快,并且调用selenium的速度比appium的速度快很多;所以在整体使用隐形等待的基础上,每新进入1个页面\页面刷新等操作时,需要添加1s的sleep强制等待(预防,避免出现错误)

