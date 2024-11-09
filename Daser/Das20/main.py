import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="testpy2",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()
create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

# insert = '''
#     INSERT INTO users (username, password) VALUES (%s, %s)
# '''
# cursor.execute(insert, ("Vardan", "1234",))
# connection.commit()

# delete = '''
#     DELETE FROM users WHERE username = (%s);
# '''
# cursor.execute(delete, ("Karen",))
# connection.commit()

# def delete(delete_input):
#     delete = '''
#         DELETE FROM users WHERE password = (%s);
#     '''
#     cursor.execute(delete, (delete_input,))
#     connection.commit()
#     return True

# while True:
#     delete_input2 = input("Greq Passwordy:  ")
#     if delete(delete_input=delete_input2):
#         print("Procces Succesed")
#         break
#     else:
#         print("An error try again")

# update = '''
#     UPDATE users SET username = %s WHERE id = %s;
# '''
# cursor.execute(update, ("Davit", "1",) )
# connection.commit()

# def popoxum(update_input, password):
#     update = '''
#         UPDATE users SET username = (%s) WHERE password = (%s);
#     '''
#     cursor.execute(update, (update_input, password,))
#     connection.commit()
#     return True

# while True:
#     update_input2 = input("Greq Te inch anunneq uzum poxel:  ")
#     Password = input("Password:   ")   
#     if popoxum(update_input=update_input2, password=Password):
#         print("Dzer Tvyalnery Hajpxoutyamb Popoxvecin")
#         break

#insert

# insert = '''
#     INSERT INTO users (username, password) VALUES (%s, %s)
# '''
# cursor.execute(insert, ("Karen", "123456"))
# connection.commit()

#select

# select = '''
#     SELECT * FROM users WHERE id = (%s);
# '''
# cursor.execute(select, ("5"))
# users = cursor.fetchall()
# users2 = cursor.fetchone()
# print(users)
# print(users2)


#delete

# delete = '''
#     DELETE FROM users WHERE id = (%s);
# '''
# cursor.execute(delete, ("1",))
# connection.commit()

#update

# update = '''
#     UPDATE users SET username = (%s) WHERE id = (%s);
# '''

# cursor.execute(update, ("Edvard", "3",))
# connection.commit()


