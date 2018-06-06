import unittest,time,HTMLTestRunner
from BeautifulReport import BeautifulReport
from config.globalpara import test_case_path,current_time,report_path,report_name
from common.send_mail import Send_mail
import time
#构造测试集，覆盖test开头测试用例
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path,pattern='test*.py')


if __name__ == '__main__':


    # report = report_name+'report.html'
    # fb = open(report,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fb,
    #     title='测试报告',
    #     description='结果描述'
    # )
    # runner.run(suite)
    # fb.close()
#美化报告
    result = BeautifulReport(suite)
    result.report(filename=current_time,description='接口测试报告',log_path=report_path)

    time.sleep(3)
    email = Send_mail()
    email.sendReport()

