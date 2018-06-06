import time,os

#项目路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#测试用例代码存放路径
test_case_path = project_path + '\\testCase'
test_data = project_path+'\\testFile\\'
#日志文件存放路径
log_path = project_path + '\\log\\mylog.log'
#测试报告存放路径
report_path = project_path + '\\report\\'
report_name = report_path + time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
#格式化当前时间
current_time = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())

#小题host
xiaoti = 'http://xtapi.yx'
#小文host
xiaowen = 'http://xwapi.yx'
#小点host
xiaodian = 'http://xdapi.yx'
#邮箱
send_user = '1633882338@qq.com'
mail_password = 'fzxlihovutrucdfd'
mail_host = 'smtp.qq.com'

#接收邮箱
receive = 'xuejiling@classba.cn','377169099@qq.com'
# print(project_path)
# print(test_case_path)
# print(log_path)
# print(img_path)
