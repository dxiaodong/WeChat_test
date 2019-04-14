"""
1.学习目标
    掌握微信小程序自动化测试方法
2.操作步骤
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
        "chromeOptions":{"androidProcess":"com.tencent.mm:appbrand2"}
3. 需求
    进入微信,选择摩拜单车小程序,进入个人中心,点击我的卡券
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
desired_caps['chromeOptions'] = {"androidProcess":"com.tencent.mm:appbrand0"}
# >>3. 声明驱动对象
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print('成功打开微信')
time.sleep(20)
# >>4.下滑屏幕
def swipe_down(driver,time=500,n=1):
    """向下滑动"""
    size = driver.get_window_size()
    x1 = size['width']*0.5
    y1 = size['height']*0.25
    y2 = size['height']*0.75

    for i in range(n):
        driver.swipe(x1,y1,x1,y2,time)

swipe_down(driver)
# >>5.进入小程序--摩拜单车
driver.find_element_by_xpath('//android.widget.TextView[@text = "摩拜单车"]').click()
print('进入摩拜单车首页')
time.sleep(30)
# >>6.点击个人中心
# TouchAction(driver).tap(x=950,y=1600).perform()
# driver.tap([(872,1519),(1078,1725)])
TouchAction(driver).press(x=950,y=1600).release().perform()
print('进入个人中心')
# >>7.点击我的卡券
time.sleep(10)
driver.find_element_by_xpath('//android.view.View[@text="我的卡券"]').click()
print('进入我的卡券')
time.sleep(5)
driver.get_screenshot_as_file('我的卡券.png')




