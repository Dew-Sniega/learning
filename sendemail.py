import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'misakiruby@126.com'
msg['to'] = 'Dew_Sniega@163.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com', '25')
smtp.login('misakiruby@126.com', 'WRWNFCW97#')
smtp.sendmail('misakiruby@126.com', 'Dew_Sniega@163.com', str(msg))
smtp.quit()
