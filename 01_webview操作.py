"""
1. 学习目标
    掌握app页面的webview页面操作
2. 实现步骤
    2.1 获取所有上下文
        driver.contexts
    2.2 进入webview页面
        driver.switch_to.context(webview页面的context)
    2.3 操作webview页面
        方式同selenium一致
    2.4 跳出webview页面
        driver.switch_to.context(native页面)
3. 需求
    打开百度APP,进入登录页面,选择微博登录

"""
#com.baidu.searchbox.lite/com.baidu.searchbox.MainActivity
# >>1. 导入appium
from appium import webdriver
import time

# >>2. 配置 server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'# 系统名称
desired_caps['platformVersion'] = '5.1.1'# 系统版本
desired_caps['deviceName'] = '192.168.77.101:5555'# 设备名称
# app 信息
desired_caps['appPackage'] = 'com.baidu.searchbox.lite'# 需要启动的APP包名
desired_caps['appActivity'] = 'com.baidu.searchbox.MainActivity'# 需要启动的APP启动名
# 输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# >>3. 声明驱动对象
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print('成功打开百度APP')
time.sleep(20)
# >>4. 进入个人中心
driver.find_element_by_xpath('//android.widget.TextView[@text="未登录"]').click()
# >>5. 点击微博登录
driver.find_element_by_id('com.baidu.searchbox.lite:id/hd').click()
# >>6. 获取所有contexts
contexts = driver.contexts
print(contexts)
# >>7. 进入webview
driver.switch_to.context('WEBVIEW_com.baidu.searchbox.lite')
print('成功进入webview')
time.sleep(10)
# >>8.在webview中输入微博用户名密码
driver.find_element_by_id('loginName').send_keys('中文名')
driver.find_element_by_id('loginPassword').send_keys('123456')
# >>9.跳出webview
driver.switch_to.context(contexts[0])
# >>10.点击返回键
driver.find_element_by_xpath('//android.widget.TextView[@text = "关闭"]').click()
