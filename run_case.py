# coding:utf-8
import      HTMLTestReportCN
import time
import  unittest
import smtplib                             # 邮件相关的库
from email.mime.text import MIMEText        #相当于一张纸
from email.mime.multipart import MIMEMultipart


def   report_test():
        '''第一步:加载test_case下所有的测试用例,并运行生成测试报告'''
        test_dir = r"G:\pyCharm\Script\python_automated_testing\test_case"
        # discover方法加载多个用例集合
        discover = unittest.defaultTestLoader.discover(start_dir= test_dir,
                                                       pattern="test*.py",
                                                     top_level_dir=None)
        # 用testsuit收集测试用例
        test_suit = unittest.TestSuite()
        test_suit.addTest(discover)
        print(discover)

        # 获取当前时间;测试报告存放路径和取名;文件读取
        nowTime = time.strftime("%Y-%m-%d")
        report_file = "G:\\pyCharm\\Script\\python_automated_testing\\%s-reporttest.html"%nowTime
        fp = open(report_file,"wb")
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                              title=u"%测试报告",
                                              description=u"%s自动生成测试报告"%nowTime )
        runner.run(discover)

def send_email():
    #发送邮件
    smtpserver = "smtp.qq.com"      # 发件服务器
    port = 465                      # 端口号对应
    user = "314983713@qq.com"       # 发件人邮件
    psw = "yqcclsgwyldwbjag"        # 登录秘钥
    receiver = "1315270232@qq.com"  # 收件人邮箱

    #  正文部；获取当前时间
    nowTime = time.strftime("%Y-%m-%d")
    b = open("%s-reporttest.html" % nowTime, "r", encoding='utf-8')  #打开测试报告的路径
    mail_body = b.read()
    b.close()


    msg = MIMEMultipart()
    msg["from"] = user              # 发件人
    msg["to"] = receiver            # 收件人
    msg["subject"] = "软件测试报告"   # 主题

    # 正文内容
    body = MIMEText(mail_body,"html", "utf-8")
    msg.attach(body)

    # 附件内容
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="%s-reporttest.html"'%nowTime
    msg.attach(att)
    smtp = smtplib.SMTP_SSL(smtpserver, port)       # 连接QQ服务器
    smtp.login(user, psw)                           # 登录成功，传人账号和密码
    smtp.sendmail(user, receiver, msg.as_string())  # 发送邮件；发件人邮件；收件人邮箱
    smtp.quit()   # 退出


if __name__ == '__main__':
    report_test()
    #send_email()

