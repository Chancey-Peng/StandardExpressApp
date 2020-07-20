'''
    Appium Webdriver utils.
    Easy to use appium webdriver method.
'''
import os
import sys
import time
import unittest
from time import sleep
from appium import webdriver
from config import globalparameter as GL
from src.common import log

utils_log = log.log()

def wait_time(func):
    def inner(*args):
        time.sleep(0.5)
        f = func(*args)
        time.sleep(0.5)
        return f
    return inner

# element locators: click
def el_id_click(driver, element):
    try:
        return driver.find_element_by_id(element).click()
    except:
        utils_log.error(u'找不到元素' + str(element))

def el_class_click(driver, element):
    try:
        return driver.find_element_by_class_name(element).click()
    except:
        utils_log.error(u'找不到元素' + str(element))


def el_xpath_click(driver, element):
    try:
        return driver.find_element_by_xpath(element).click()
    except:
        utils_log.error(u'找不到元素' + str(element))


# action
def el_send_keys(driver, element, data):
    try:
        return driver.find_element_by_id(element).send_keys(data)
    except:
        utils_log.error(u'找不到元素' + str(element))


def el_text(driver, element):
    try:
        return driver.find_element_by_id(element).text
    except:
        utils_log.error(u'找不到元素' + str(element))


@wait_time
def screenshot(driver, img_name):
    try:
        filename = ''.join(GL.img_path + "_"+ img_name + ".png")
        return driver.get_screenshot_as_file(filename)
    except:
        utils_log.error(u'截图失败：' + img_name)


# page element check
def el_check(driver, element):
    """
    使用此方法检测某个元素是否在页面上
    assertTrue(el_check(element))
    """
    return driver.find_element_by_id(element).is_dispalyed()


# Swipe: Left Right Up Down
class MobileSwipe():

    def __init__(self):
        pass

    def swipe_up(self, driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width / 2, height / 4, width / 2, height / 4 * 3, 800)

    def swipe_down(self, driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width / 2, height / 4 * 3, width / 2, height / 4, 800)

    def swipe_down_half(self, driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width / 2, height / 4 * 3, width / 2, height / 4 * 2, 800)

    def swipe_left(self, driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width / 6 * 5, height / 2, width / 10, height / 2, 800)

    def swipe_right(self, driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width / 4, height / 2, width / 4 * 3, height / 2, 800)


if __name__ == "__main__":
    MobileSwipe()
    # print(os.getcwd()) # 获取当前目录