import bcrypt
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="hashedlogin",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        mail TEXT NOT NULL,
        password BYTEA NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()


def signup_or_signin(choice1=None, choice2=None):
    if choice1 == "signup":
        return True
    elif choice2 == "signin":
        return True
    return False


while True:
    harcum1 = input("Գրանցվել կամ մուտք գործել (SignUp or SignIn): ")
    
    if signup_or_signin(choice1=harcum1):
        user_mail = input("Մուտքագրեք էլփոստը: ")
        user_password = input("Մուտքագրեք գաղտնաբառը: ").encode()
        password_hashed = bcrypt.hashpw(user_password, bcrypt.gensalt(rounds=12))
        
        insert = '''
            INSERT INTO users (mail, password) VALUES (%s, %s);
        '''
        cursor.execute(insert, (user_mail, password_hashed))
        connection.commit()
        print("Դուք գրանցվել եք հաջողությամբ!")
    
    elif signup_or_signin(choice2=harcum1):
        user_mail = input("Մուտքագրեք էլփոստը: ")
        user_password = input("Մուտքագրեք գաղտնաբառը: ").encode()
        
        select = '''
            SELECT * FROM users WHERE mail = %s;
        '''
        cursor.execute(select, (user_mail,))
        user = cursor.fetchone()
        
        if user:
            db_password = bytes(user[2])  
            if bcrypt.checkpw(user_password, db_password):
                print("Բարի գալուստ ձեր էջ!")
            else:
                print("Սխալ էլփոստ կամ գաղտնաբառ")
        else:
            print("Օգտագործողը չգտնվեց")


# text = b"Hello"
# hashed = bcrypt.hashpw(text, bcrypt.gensalt(rounds=12))
# print(hashed)

# print(bcrypt.checkpw(b'Barev', hashed))

# user_password = input("enter password").encode()
# hashed = bcrypt.hashpw(user_password, bcrypt.gensalt(rounds=12))

# password2 = input("Greq mutqi passwordy: ").encode()
# re_hashed = bcrypt.checkpw(password2, hashed)

# if re_hashed:
#     print("Bari Galust dzer ej")
# else:
#     print("Sxal gaxtnabar")
