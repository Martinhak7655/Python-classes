import psycopg2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

connection = psycopg2.connect(
    host="localhost",
    database="web_site",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()
create_table = '''
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    mail VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''
cursor.execute(create_table)
connection.commit()

Name = input("Name:  ")
Mail = input("Mail:  ")
Password = input("Password:  ")
Verify = int(input("Verify code:  "))

random_number = random.randint(1000, 9999)
msg = MIMEMultipart()
msg['From'] ="martinhakobyan2024@mail.ru"
msg['To'] = "martinhakobyan954@gmail.com"
msg['Subject'] = "Hastateq dzer mail hascen"
msg.attach(MIMEText( f"Mek angamva ogtagorcman kod - {random_number}", 'plain'))
server = smtplib.SMTP_SSL("smtp.mail.ru", 465)

server.login("martinhakobyan2024@mail.ru", "hdarqJ25g0Msx1Trk9eF")
server.sendmail("martinhakobyan2024@mail.ru", "martinhakobyan954@gmail.com", msg.as_string())


def grancum(name, mail, password, verify):
        if name != "" and len(password) >= 8:
            msg = MIMEMultipart()
            msg['From'] ="martinhakobyan2024@mail.ru"
            msg['To'] = "martinhakobyan954@gmail.com"
            msg['Subject'] = "Hastateq dzer mail hascen"
            msg.attach(MIMEText( f"Mek angamva ogtagorcman kod - {random_number}", 'plain'))
            server = smtplib.SMTP_SSL("smtp.mail.ru", 465)

            server.login("martinhakobyan2024@mail.ru", "hdarqJ25g0Msx1Trk9eF")
            server.sendmail("martinhakobyan2024@mail.ru", "martinhakobyan954@gmail.com", msg.as_string())

            if verify == random_number:
                insert = '''
                    INSERT INTO users (username, mail, password) VALUES (%s, %s, %s)
                '''
                cursor.execute(insert, (name, mail, password))
                connection.commit()
                print("Succesfull")
                return True
        return False

while True:
    Name = input("Name:  ")
    Mail = input("Mail:  ")
    Password = input("Password:  ")
    Verify = int(input("Verify code:  "))
    if grancum(name=Name, mail=Mail, password=Password, verify=Verify):
        print("Succesed Process")
        break
    else:
        print("-"*25)
        print("An error try again")
        print("-"*25)

