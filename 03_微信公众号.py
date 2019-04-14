"""
1. 学习目标
    掌握微信公众号操作方式
2. 操作步骤
    2.1 连接真机,获取真机devicesName
        adb devices
    2.2 获取微信包名和启动名
        打开微信,命令行输入adb shell dumpsys window windows | findstr mFocusedApp
        微信包名:com.tencent.mm
        微信启动名:.ui.LauncherUI
    2.3 获取小程序进程
        进入adb shell 命令
        ① 查询pid
            dumpsys activity top | grep ACTIVITY
        ② 根据pid查找进程
            ps pid
            com.tencent.mm:appbrand3
    2.4 前置代码增加选择:
        "chromeOptions":{"androidProcess":"com.tencent.mm:tools"}
    2.5 打开微信X5调试页面
3. 需求
    打开微信,进入国美管家公众号,点击家电回收,点击手机回收
"""
# >>1. 导入appium
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

# >>2. 配置 server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'# 系统名称
desired_caps['platformVersion'] = '7.1.1'# 系统版本
desired_caps['deviceName'] = '192.168.77.101:5555'# 设备名称
# app 信息
desired_caps['appPackage'] = 'com.tencent.mm'# 需要启动的APP包名
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'# 需要启动的APP启动名
# 输入中文
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True
# 不重置应用
desired_caps['noReset'] = True
# 启动微信小程序
desired_caps['chromeOptions'] = {"androidProcess":"com.tencent.mm:tools"}
# >>3. 声明驱动对象
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print('成功打开微信')
time.sleep(20)
# >>4. 点击通讯录
driver.find_element_by_xpath('//*[@text = "通讯录"]').click()
time.sleep(3)
# >>5. 点击公众号按钮
driver.find_element_by_xpath('//*[@text = "公众号"]').click()
time.sleep(3)
# 进入被测公众号
driver.find_element_by_xpath('//*[@text = "国美管家"]').click()
time.sleep(3)
# 点击抢福利
driver.find_element_by_xpath('//*[contains(@text,"预约服务")]').click()
time.sleep(6)
# 判断页面是否是webView
contexts = driver.contexts
for context in contexts:
# 打印
    print(context)
# 切换到webview模式查找元素
driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
print("进入webview")
time.sleep(5)
# 点击家电回收
driver.find_element_by_link_text('家电回收').click()
print('进入家电回收页面')
time.sleep(2)
# 点击手机回收
driver.find_element_by_xpath('//ul[@class="clearfix"]/li[1]/a').click()
print('进入手机回收页面')
