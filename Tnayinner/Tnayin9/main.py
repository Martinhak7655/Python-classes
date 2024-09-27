import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

msg = MIMEMultipart()
msg['From'] = 'thedavitmanukyan@mail.ru'
msg['To'] = 'martinhakobyan954@gmail.com'
msg["Subject"] = 'Hastateq Dzer Mail hascen'
random_num = random.randint(1000, 9999)
msg.attach(MIMEText( f"Mek angamva ogtagorcman kod - {random_num}", 'plain'))
server = smtplib.SMTP_SSL("smtp.mail.ru", 465)

server.login("thedavitmanukyan@mail.ru", "y0xG0CGX5hntimArxVK8")

server.sendmail("thedavitmanukyan@mail.ru", "martinhakobyan954@gmail.com", msg.as_string())

user = int(input("Greq Emailin uxarkvac kody>>>> "))

if user == random_num:
    print("Chist e anceq araj")