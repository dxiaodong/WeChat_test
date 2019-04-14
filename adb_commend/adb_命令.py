import subprocess
import re

def getDevice():
    """获取设备名称"""
    device = []
    result = subprocess.Popen("adb devices", shell=True, stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    # print(result)

    for item in result:
        t = item.decode().split("\tdevice")
        # print(t)
        if len(t) >= 2:
            device.append(t[0])
    return device

def getPackageAndActivity(apk_path):
    """获取包名和启动类名"""
    sub_p = subprocess.Popen("aapt dump badging %s" % apk_path, shell=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, error) = sub_p.communicate()
    # print(output)
    package = re.compile("package: name='(\S+)'").search(output.decode())
    #print(package.group(1))
    if package is not None:
        apppackage = package.group(1)
    activity = re.compile("launchable-activity: name='(\S+)'").search(output.decode())
    #print(activity.group(1))
    if activity is not None:
        appactivity = activity.group(1)
    return apppackage,appactivity


if __name__ == '__main__':
    print(getDevice())
    apk_path = r"E:\untitled\MyAppiumDmeo\APP\Qunar.apk"
    print(getPackageAndActivity(apk_path))

