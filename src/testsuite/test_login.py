import os
import re
import sys
import time
import unittest
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

# sys.path.append("..")
from config import appium_config
from config import globalparameter as GL
from src.common.utils import el_id_click, el_xpath_click, el_text, el_send_keys
from src.common.utils import screenshot
from src.common.utils import MobileSwipe

# config.ini
cfg = ConfigParser()
a = cfg.read(GL.config_file_path)

def handle_page_return(driver, el):
    """
    当从下级页面返回到上级页面时,因元素无法定位或发生异常时,使用系统返回键返回，从而不影响后续case执行。
    :param driver:
    :param el:
    :return:
    """
    try:
        el_id_click(driver, el)
    except Exception as e:
        print(e)
        driver.keyevent(4)

class Login(unittest.TestCase):
    """
    TestCase: Goods
    Description: 1.元素点击 2.截图 3.点击左上角返回按钮
    """

    # @classmethod,在此类中只进行一次初始化和清理工作
    @classmethod
    def setUpClass(self):
        self.driver = appium_config.appium_start()
        self.swipe = MobileSwipe()

    def test_initial(self):
        """
        首页:首页初始页面
        """
        if self.driver.current_activity != ".activity.MainActivity":
            self.driver.implicitly_wait(20)
        time.sleep(3)
        agree = el_id_click(self.driver, cfg.get("start","agree"))
        call_allow = el_id_click(self.driver, cfg.get("miui","call_allow"))
        laction_only = el_id_click(self.driver,cfg.get("miui", "laction_only"))
        rw_allow = el_id_click(self.driver, cfg.get("miui", "rw_allow"))
        time.sleep(5)
        # for n in range(5):
        #     self.swipe.swipe_left(self.driver)
        for i in range(3):
            self.driver.swipe(700, 200, 100, 200, 500)  # 滑屏三次
        time.sleep(3)
        start_login = el_id_click(self.driver, cfg.get("experience", "start_login"))


    def test_start_login(self):
        tel = el_send_keys(self.driver, cfg.get("login", "tel"), GL.login_username)
        pwd = el_send_keys(self.driver, cfg.get("login", "pwd"), GL.login_password)
        login = el_id_click(self.driver, cfg.get("login", "login"))
        screenshot(self.driver)

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()
        


# texture Testcase
def suite_goods():
    tests = [
        "test_initial",
        "test_start_login"

    ]
    return unittest.TestSuite(map(Login, tests))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=3).run(suite_goods())