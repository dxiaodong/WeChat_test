import re
from math import floor
import subprocess
import os
import json
'''
apk文件的读取信息
'''
class ApkInfo():
    def __init__(self, apkPath):
        self.apkPath = apkPath
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (self.output, err) = p.communicate()

# 得到app的文件大小
    def getApkSize(self):
        size = floor(os.path.getsize(self.apkPath) / (1024 * 1000))
        return str(size) + "M"


    def getApkBaseInfo(self):

        match = re.compile("package: name='(\S+)'").match(self.output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        apppackage = match.group(1)
        #appactivity = match.group(2)

        # print('packagename:' + packagename)
        # print('versionCode:' + versionCode)
        # print('versionName:' + versionName)
        return apppackage

    #得到应用名字
    def getApkName(self):
        t = self.output.decode().split()
        for item in t:
            # print(item)
            match = re.compile("application-label:(\S+)").search(item)
            if match is not None:
                return match.group(1)

    #得到启动类
    def getApkActivity(self):
        print("=====getApkActivity=========")
        match = re.compile("launchable-activity: name=(\S+)").search(self.output.decode())
        #print("match=%s" %match)
        if match is not None:
            return match.group(1)
if __name__ == '__main__':
    pass
    app = ApkInfo("E:\\untitled\\MyAppiumDmeo\\APP\\Qunar.apk")
    print(app.getApkBaseInfo())


    # ApkInfo(r"D:\app\appium\Img\Jianshu-2.3.1.apk").getApkActivity()
    # # ApkInfo(r"D:\app\appium_study\Img\t.apk").get_apk_version()
    # # ApkInfo(r"D:\app\appium_study\Img\t.apk").get_apk_name()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_activity()
    # ApkInfo(r"D:\app\appium_study\Img\t.apk").get_apk_activity()


