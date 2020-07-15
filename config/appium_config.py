# import os
# import sys
# import time
# import re
from appium import webdriver

# sys.path.append("..")
# device_id = get_serialno()

# os_version = os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_id)).read()

def appium_start():
    config = {
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "e6d9f02f",
        "appPackage": "com.bxkc.android",
        "appActivity": "com.bxkc.android.activity.WelcomeActivity",

        'newCommandTimeout': 30,
        'automationName': 'Appium',
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }

    return webdriver.Remote('http://localhost:4723/wd/hub', config)

if __name__=='__main__':
    appium_start()