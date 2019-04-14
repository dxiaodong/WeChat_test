"""
需求:
    从微信进入源码时代公众号,进入课程简介,浏览课程简介,找到软件测试课程,进入
总结:
    1. app_native页面滑动可以边滑动,边寻找元素
    2. app_webview页面滑动操作,可直接滑动到指定元素位置
        使用js方法,直接滑动到该元素
        js = "arguments[0].scrollIntoView(true)"
        driver.execute_script(js,要滑动到位置的元素)

"""
# >>1. 导入appium
from appium import webdriver
import time

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
def swipe_up(driver,time=3000,n=1):
    """向下滑动"""
    size = driver.get_window_size()
    x1 = size['width']*0.5
    y1 = size['height']*0.75
    y2 = size['height']*0.25
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,time)
# >>6. 滑动并找到源码时代公众号--进入
while True:
    try:
        driver.find_element_by_xpath('//android.widget.TextView[@text="源码时代"]').click()
        break
    except:
        swipe_up(driver)
print('成功进入源码时代微信公众号')
time.sleep(5)
# >>7. 点击初始按钮
driver.find_element_by_xpath('//android.widget.TextView[@text="初识"]').click()
# >>8. 选择课程简介
driver.find_element_by_xpath('//android.widget.TextView[@text="课程简介"]').click()
time.sleep(10)
# >>9. 滑动并找到软件测试
#swipe_up(driver,500,3)

# >>10. 获取webview--contexts
contexts = driver.contexts
print(contexts)
# >>11. 进入webview页面
driver.switch_to.context(contexts[1])
print('进入webview页面')
# >>12. 点击软件测试课程
js = "arguments[0].scrollIntoView(true)"
test = driver.find_element_by_xpath('/html/body/div[10]/a/img')
driver.execute_script(js,test)
time.sleep(3)
test.click()
# >>13, 关闭微信
driver.quit()



