# import os
# import sys
# import time
# import unittest
#
# from configparser import ConfigParser
# from selenium import webdriver
# from appium import webdriver
#
# sys.path.append("..")
# from config.appium_config import appium_start
#
# # 读取config.ini
# cfg = ConfigParser()
# cfg.read("../config/config.ini")
#
# def handle_page_return(driver,el):
#     """
#     当从下级页面返回到上级页面时,因元素无法定位或发生异常时,
#     使用系统返回键返回，从而不影响后续case执行。
#     """
#     # try:
#     #     el_id_click(driver, el)
#     # except Exception as e:
#     #     print(e)
#     #     driver.keyevent(4)

import ddt
import unittest
from src.common.excel_data import Excel
from config import globalparameter as GL
ex = Excel()
excel_data = ex.read_excel(GL.test_data_path)
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("这是setUp")

    def tearDown(self):
        print("这是tearDown")

    def test_add(self,a,b):
        print(a+b)

    # @ddt.data(
    #     ["1","2"],
    #     ["3","4"],
    #     ["5","6"]
    # )
    @ddt.data(*excel_data)
    def test_add(self,excel_data):
        # a,b,c,d,e,f,g,h,i,j,k,l = excel_data
        # print(b,c)
        print(excel_data['username'],excel_data['password'])

if __name__ == '__main__':
    unittest.main()
#
# import ddt
# import unittest
# from src.common import excel_data
# class FirtDDTCase(unittest.TestCase):
#
#     @ddt.data(*data)