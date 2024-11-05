# import psycopg2
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# connection = psycopg2.connect(
#     host="localhost",
#     database="Qnutyun1",
#     user="postgres",
#     password="MH2012"
# )

# cursor = connection.cursor()
# create_table = '''
#     CREATE TABLE IF NOT EXISTS users(
#         id SERIAL PRIMARY KEY,
#         username VARCHAR(100) NOT NULL,
#         password VARCHAR(100) NOT NULL,
#         create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     );
# '''
# cursor.execute(create_table)
# connection.commit()

# insert = '''
#     INSERT INTO users (username, password) VALUES (%s, %s);
# '''
# cursor.execute(insert, ("Aram", "1234567890",))
# connection.commit()

# select = '''
#     SELECT * FROM users Where username = (%s);
# '''
# cursor.execute(select, ("Erik",))
# connection.commit()
# user = cursor.fetchone()
# for x in user:
#     print(x)

# select = '''
#     SELECT * FROM users;
# '''
# cursor.execute(select)
# connection.commit()
# user = cursor.fetchall()
# for x in user:
#     print(x)

# def harcum(harc1=None, harc2=None):
#     if harc1 == "grancvel":
#         return True
#     elif harc2 == "mutq gorcel":
#         return True
#     else:
#         return False


# def grancum(user, password):
#     if user != "" and len(password) >= 8:
#         insert = '''
#             INSERT INTO users (username, password) VALUES(%s, %s);
#         '''
#         cursor.execute(insert, (user, password,))
#         connection.commit()
#         return True
#     return False

# def mutq_gorcel(password2):
#     select = '''
#         SELECT * FROM users WHERE password = (%s);
#     '''
#     cursor.execute(select, (password2,))
#     users = cursor.fetchone()
#     for x in users:
#         print(x)

# while True:
#     hastatel = input("Duq cankanumeq grancvel te mutq gorcel")
#     if harcum(harc1=hastatel):
#         User = input("Name:  ")
#         Password = input("Password:  ")
#         if grancum(user=User, password=Password):
#             print("Dzer Tvyalnery Hajoxutyamb grancvecin")
#         else:
#             print("-" *25)
#             print("Sxale Noric pordzeq")
#             print("-" *25)
#     elif harcum(harc2=hastatel):
#         Password2 = input("Greq passwordy")
#         if mutq_gorcel(password2=Password2):
#             print("Procces Succesed")
#         else:
#             print("Sxale Noric Pordzeq")
#     else:
#         print("-" *25)
#         print("Aydpisi hraman chka")
#         print("-" *25)

# msg = MIMEMultipart()
# msg["From"] = "martinhakobyan2024@mail.ru"
# msg["To"] = "martinhakobyan954@gmail.com"
# msg["Subject"] = "Web Site"
# msg.attach(MIMEText(f"Bari Galust Dzer Ej", 'plain'))

# server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
# server.login("martinhakobyan2024@mail.ru", "RiKwazqbCt9c9kAuYdRF")
# server.sendmail("martinhakobyan2024@mail.ru", "martinhakobyan954@gmail.com", msg.as_string())
