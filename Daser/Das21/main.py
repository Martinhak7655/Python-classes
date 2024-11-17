import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="socialmedia",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        mail VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        friends_count INT DEFAULT 0
    );
'''
cursor.execute(create_table)
connection.commit()

def harcum(harc1=None, harc2=None):
    if harc1 == "Grancvel":
        return True
    elif harc2 == "Mutq gorcel":
        return True
    else:
        return False

def signin(name, mail, password):
    if name == "" or mail == "" or password == "":
        return False
    insert = '''
        INSERT INTO users (name, mail, password, friends_count) VALUES (%s, %s, %s, %s);
    '''
    cursor.execute(insert, (name, mail, password, 0,))
    connection.commit()
    return True

def signup(mail, password):
    if mail == "" or password == "":
        return False
    select = '''
        SELECT FROM users WHERE mail = (%s) AND password = (%s);
    '''
    cursor.execute(select, (mail, password,))
    connection.commit()
    return True

def see_all():
    select = '''
        SELECT * FROM users;
    '''
    cursor.execute(select)
    connection.commit()
    users = cursor.fetchall()
    for x in users:
        print(f'Name: {x[1]} Mail: {x[2]}')
    return True

def friends_add(username, mail):
    if username == "" or mail == "":
        return False
    update = '''
        UPDATE users SET friends_count = friends_count + 1 WHERE name = (%s) AND mail = (%s);      
    '''
    cursor.execute(update, (username, mail,))
    connection.commit()
    return True

def see_my_all_friends(mail):
    if mail == "":
        return False
    select = '''
        SELECT * FROM users WHERE mail = (%s);
    '''
    cursor.execute(select, (mail,))
    connection.commit()
    users = cursor.fetchone()

    print(f"Dzer Ynkereneri tivy` {users[4]}")
    return True

while True:
    harc = input("Grancvel te Mutq gorcel")
    if harcum(harc1=harc):
        username = input("Username:  ")
        mail = input("Mail:  ")
        password = input("Password:  ")
        if signin(name=username, mail=mail, password=password):
                print("-" * 25)
                print("Nayel Bolor ejery:  J")
                print("Add tal urishin: A")
                print("Nayel im hetevordneri qanaky: S")
                print("Exit: E")
                print("-" * 25)
                while True:
                    command = input("Command:  ")
                    if command == "J":
                        see_all()
                        print("Succes Proccesed")
                    elif command == "A":
                        username = input("Greq anuny:  ")
                        mail = input("Greq nra maily:  ")
                        if friends_add(username=username, mail=mail):
                            print("Succesed Procces")
                    elif command == "S":
                        mail = input("Greq dzer maily")
                        if see_my_all_friends(mail=mail):
                            print("Succes Proccesed")
                    elif command == "E":
                        print("Succes")
                        break
    elif harcum(harc2=harc):
        mail = input("Mail:  ")
        password = input("Password:  ")
        if signup(mail=mail, password=password):
                print("-" * 25)
                print("Nayel Bolor ejery:  J")
                print("Add tal urishin: A")
                print("Nayel im hetevordneri qanaky: S")
                print("Exit: E")
                print("-" * 25)
                while True:
                    command = input("Command:  ")
                    if command == "J":
                        print(f"Succes Proccesed{see_all()}")
                    elif command == "A":
                        username = input("Greq anuny:  ")
                        mail = input("Greq nra maily:  ")
                        if friends_add(username=username, mail=mail):
                            print("Succesed Procces")
                    elif command == "S":
                        mail = input("Greq dzer maily")
                        if see_my_all_friends(mail=mail):
                            print("Succes Proccesed")
                    elif command == "E":
                        print("Succes")
                        break
