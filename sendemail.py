import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'Dew_Sniega@163.com'
msg['to'] = '1205620040@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('Dew_Sniega@163.com', 'wrwnfcw97')
smtp.sendmail('Dew_Sniega@163.com', '1205620040@qq.com', str(msg))
smtp.quit()
