import unittest
import time
from config import globalparameter as GL
from src.common import HTMLTestRunner

"""构建测试套件，并执行测试"""

# 构建测试集，包含src/testsuite目录下的所有以test开头的.py文件
# print(test_case_path)
print(GL.report_name)
suite_runner = unittest.defaultTestLoader.discover(start_dir=GL.test_case_path,pattern="test*.py")

if __name__ == "__main__":
    report = ''.join(GL.report_name + ".html")
    fb = open(report,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title=u"标讯快车自动化测试报告", description=u"这是一个登录测试报告")
    runner.run(suite_runner)
    fb.close()