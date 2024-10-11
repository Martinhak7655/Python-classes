import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mail():
    msg = MIMEMultipart()
    msg["From"] = "thedavitmanukyan@mail.ru"
    msg["To"] = "martinhakobyan954@gmail.com"
    msg["Subject"] = "Mutq Gorcum"
    msg.attach(MIMEText("Zgushacum!!! Dzer Kayq Marde Mutq gorcel"))
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login("thedavitmanukyan@mail.ru", "y0xG0CGX5hntimArxVK8")
    server.sendmail("thedavitmanukyan@mail.ru", "martinhakobyan954@gmail.com", msg.as_string())

user = [
    {
        "name": "Martin",
        "mail": "test@gmail.com",
        "password": "3456"
    }
]

harcum = input("duq cankanumeq grancvel te mutq gorcel >> ")
while True:
    if harcum == "grancvel":
        name = input("Greq Dzer Anuny >> ")
        mail = input("Greq Dzer Maily >> ")
        password = input("Greq dzer passwordy >> ")
        if len(password) >= 8:
            user2 = {
                "name": name,
                "mail": mail,
                "password": password
            }
            user.append(user2)
            break
        else:
            print("Sxale Noric Pordzeq")
            continue
    elif harcum == "mutq gorcel":
        mail2 = input("Greq accounti maily")
        password2 = input("Greq accounti passwordy")
        for i in user:
            if mail2 == i["mail"] and password2 == i["password"]:
                mail()
                print("Duq Hajoxutyamb mutq gorceciq")
                break
            print("Sxale maily kam passwordy")
            continue

