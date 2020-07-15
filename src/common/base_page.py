import os
import sys
import time
import unittest

from configparser import ConfigParser
from selenium import webdriver
from appium import webdriver

sys.path.append("..")
from config.appium_config import appium_start

# 读取config.ini
cfg = ConfigParser()
cfg.read("../config/config.ini")

def handle_page_return(driver,el):
    """
    当从下级页面返回到上级页面时,因元素无法定位或发生异常时,
    使用系统返回键返回，从而不影响后续case执行。
    """
    # try:
    #     el_id_click(driver, el)
    # except Exception as e:
    #     print(e)
    #     driver.keyevent(4)