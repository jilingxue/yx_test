import yagmail
import os
from config import globalpara as gl
from common import Log

class Send_mail:
    def __init__(self):
        self.mylog = Log.Log()
    def configMail(self):
        try:
            #配置邮箱
            self.yag = yagmail.SMTP(user=gl.send_user,password=gl.mail_password,host=gl.mail_host,port=465)
            return self.yag
        except Exception as e:
            self.mylog.error('邮箱配置错误')
            raise e

    def sendReport(self):
        #把所有报告通过列表展示
        report_list = os.listdir(gl.report_path)
        #通过时间进行排序
        report_list.sort(key=lambda fn:os.path.getmtime(gl.report_path+'\\'+fn))
        #取最新报告
        new_report = os.path.join(gl.report_path,report_list[-1])
        try:
            self.configMail().send(gl.receive,'测试报告',attachments=new_report)
            self.mylog.info('邮件发送成功')
        except Exception as e:
            raise e
            self.mylog.error('邮件发送失败')
            #raise e





# yag = yagmail.SMTP(user='1633882338@qq.com',password='fzxlihovutrucdfd',host='smtp.qq.com',port=465)
# contents = ['this is mail']
# yag.send('xuejiling@classba.cn','subject',contents)