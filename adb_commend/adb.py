import subprocess,re

def get_device():
    """获取device"""
    result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    # print(result)
    device = []
    for item in result:
        t = item.decode().split("\tdevice")
        # print(t)
        if len(t) >= 2:
            device.append(t[0])
    #print(device)
    return device

def get_apppackage_and_appactivity(apk_path):
    sub_p = subprocess.Popen("aapt dump badging %s" % apk_path, shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    (output, error) = sub_p.communicate()
    # print(output)
    package = re.compile("package: name='(\S+)'").match(output.decode())
    if package is not None:
        apppackage = package.group(1)
    activity = re.compile("launchable-activity: name='(\S+)'").search(output.decode())
    if activity is not None:
        appactivity = activity.group(1)

    return apppackage,appactivity

if __name__ == '__main__':
    apk_path = 'baidujisuban_20514176.apk'
    print(get_device()[0])
    print(get_apppackage_and_appactivity(apk_path)[0])
    print(get_apppackage_and_appactivity(apk_path)[1])
