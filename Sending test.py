# -*- coding: utf-8 -*-
# 作者：曾晋哲
#将C:/test下的文件发送至QQ邮箱。华东师范大学计算机课专用。
print("You can send files under C:/test to your QQmail by this tool.")
QQ = input("Please input your QQ number: ")
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
import zipfile
import glob
import os
files = glob.glob('C:/test/*')
f = zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED)
for file in files:
    f.write(file, '/test/' + os.path.basename(file))
f.close()
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
from_addr = "ecnuchem2015@foxmail.com"
password = "rkzrgaqfvpjedaie"
to_addr = str(QQ) + "@qq.com"
smtp_server = "smtp.qq.com"
msg = MIMEMultipart()
msg['From'] = _format_addr(u'test文件夹发送工具 <%s>' % from_addr)
msg['To'] = _format_addr(str(QQ)+u'<%s>' % to_addr)
msg['Subject'] = Header(u'test文件夹（见附件）', 'utf-8').encode()
msg.attach(MIMEText('<b>您已收到test文件夹。</b>（见附件）', 'html', 'utf-8'))
with open('./test.zip', 'rb') as f:
    mime = MIMEBase('zip', 'zip', filename='test.zip')
    mime.add_header('Content-Disposition', 'attachment', filename='test.zip')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
server = smtplib.SMTP(smtp_server, 587) 
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
os.remove('test.zip')
