import psycopg2

# connection = psycopg2.connect(
#     host="localhost",
#     database="web_site",
#     user="postgres",
#     password="MH2012"
# )
# cursor = connection.cursor()
# create_table = '''
# CREATE TABLE IF NOT EXISTS users(
#     id SERIAL PRIMARY KEY,
#     username VARCHAR(100) NOT NULL,
#     mail VARCHAR(100) NOT NULL,
#     password VARCHAR(100) NOT NULL,
#     create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# '''
# cursor.execute(create_table)
# connection.commit()

# select = '''
#     SELECT * FROM users;
# '''
# cursor.execute(select)
# connection.commit()
# users = cursor.fetchall()
# for x in users:
#     print(x[2])

# select = '''
#     SELECT * FROM users WHERE id = (%s);
# '''

# cursor.execute(select, "1")
# connection.commit()
# users = cursor.fetchone()
# print(users)

connection = psycopg2.connect(
    host="localhost",
    database="xndirnerr",
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

def exanakner(harc1 ):
    if harc1 == "grancvel":
        return True
    else:
        return False

def exanakner2(harc2):
    if harc2 == "mutq gorcel":
        return True
    else:
        return False

def grancum(name2, mail2, password2):
    if len(password2) >= 8:
        insert = '''
            INSERT INTO users (username, mail, password) VALUES (%s, %s, %s)
        '''
        cursor.execute(insert, (name2, mail2, password2,))
        connection.commit()
        return True

def mutq_gorcel(mail_input):
    select = '''
        SELECT * FROM users WHERE mail = %s;
    '''
    cursor.execute(select, (mail_input,))
    connection.commit()
    users = cursor.fetchone()
    for x in users:
        print(x)
    return True

while True:
    harcum = input("Greq dzer grancman exanaky: grancvel te mutq gorcel >>>>   ")
    if exanakner(harc1=harcum):
        Name = input("Name:  ")
        Mail = input("Mail:  ")
        Password = input("Password:  ")
        if grancum(name2=Name, mail2=Mail, password2=Password):
            print("Dzer Tvyalnery Hajoxutyamb grancvecin")
        else:
            print("-" * 25)
            print("An error try again")
            print("-" * 25)
    elif exanakner2(harc2=harcum):
        mail_harc = input("Greq Mutq gorcman maily")
        if mutq_gorcel(mail_input=mail_harc):
            print(f"Bari galust dzer ej")
        else:
            print("-" * 25)
            print("An error try again")
            print("-" * 25)
