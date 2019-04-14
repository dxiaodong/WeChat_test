import subprocess,re

# result = subprocess.Popen('adb devices',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,
#                  stderr=subprocess.PIPE).stdout.readlines()
# print(result)
#
# devices = []
# for item in result:
#     t = item.decode().split('\tdevice')
#     print(t)
#     if len(t) >= 2:
#         devices.append(t[0])
# print(devices)
apk_path = 'baidujisuban_20514176.apk'
sub_p = subprocess.Popen(f'aapt dump badging {apk_path}',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(output,error) = sub_p.communicate()
# print(output)
# print(error)
# package = re.compile("package: name='(\S+)'").match(output.decode())
# if package is not None:
#     apppackage = package.group(1)
# print(apppackage)
# print(type(apppackage))
activity = re.compile("launchable-activity: name='(\S+)'").search(output.decode())
if activity is not None:
    appActivity = activity.group(1)
print(appActivity)
