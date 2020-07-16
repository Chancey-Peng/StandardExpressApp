# coding:utf-8
import time,os

'''
配置全局参数
'''

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# project_path1=os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]),'.'))
# print (project_path)
# print (project_path1)

#配置文件存放路径
# config_file_path = project_path + '/config/config.ini'
config_file_path = project_path + '\\config\\config.ini'
# print(config_file_path)

#execl测试数据文档存放路径
test_data_path=project_path+"\\data\\testData.xlsx"

#日志文件存储路径
log_path=project_path+"\\log\\"
log_name = log_path+time.strftime('%Y%m%d%H%S', time.localtime())

# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path+"\\report\\"
report_name = report_path+time.strftime('%Y%m%d%H%S', time.localtime())

# 异常截图存储路径,并以当前时间作为图片名称前缀
img_path = project_path+"\\error_img\\"+time.strftime('%Y%m%d%H%S', time.localtime())
# print(img_path)

#测试用例代码存放路径（用于构建suite，注意该文件夹下的文件都应该以test开头命名）
test_case_path=project_path+"\\src\\testsuite"


login_username = '13216628864'
login_password = "a123456"




if __name__=='__main__':
    test1 = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
    test2=os.path.abspath(os.path.join(test1,'testsuite'))
    print(test2)
    print(os.path.isdir(test1))
    print(os.path.isdir(test2))