"""
1. 学习目标
    掌握toast标签获取方法
2. 操作步骤
    2.1 认识toast标签
    2.2 在前置代码中添加参数
        desired_caps['automationName'] = 'uiautomator2'
    2.3 定位toast
3. 需求
    获取百度APP的toast

"""
# >>1. 导入appium
from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
# 获取toast标签
desired_caps['automationName'] = 'uiautomator2'
# 重置app
desired_caps['noReset'] = True

# >>3. 声明驱动对象
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print('成功打开百度APP')
time.sleep(20)
# >>4. 获取toast标签
# >>4.1 点击返回键
driver.keyevent(4)
#driver.back()
#print('点击返回成功')
# >>4.2 获取toast标签文本
message_loc = ("xpath","//*[contains(@text,'再按一次退出')]")
toast_element = WebDriverWait(driver,10,0.01).until(EC.presence_of_element_located(message_loc))
# toast_element = driver.find_element_by_xpath('//*[contains(@text,"再按一次退出")]')
print(toast_element.text)


time.sleep(3)

# >>5.关闭app
driver.quit()