import psycopg2
import random

connection = psycopg2.connect(
    host="localhost",
    database="quizizgame",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()


create_table = '''
    CREATE TABLE IF NOT EXISTS quiziz(
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(100) NOT NULL,
        point INTEGER DEFAULT 0,
        defeat INTEGER DEFAULT 0,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()


user_id = str(random.randint(1000, 9999))
insert = 'INSERT INTO quiziz (user_id) VALUES (%s);'
cursor.execute(insert, (user_id,))
connection.commit()

print(f"Your ID is: {user_id}")


def get_random_number(length):
    number = ''
    for _ in range(length):
        number += str(random.randint(0, 9))
    return number


def feedback(random_number, user_number):
    numbers_in = 0
    numbers_in_place = 0

    if user_number == random_number:
        return True

    for i in range(len(random_number)):
        if user_number[i] == random_number[i]:
            numbers_in_place += 1
        elif user_number[i] in random_number:
            numbers_in += 1

    print(f"Numbers in: {numbers_in}, Numbers in place: {numbers_in_place}, random_number: {random_number}")
    return False

while True:
    length = int(input("Enter number length (at least 4): "))
    if length >= 4:
        break
    print("Length too small")


random_number = get_random_number(length)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    user_input = input(f"Enter a {length}-digit number (Attempts left: {max_attempts - attempts}): ")

    if len(user_input) != length or not user_input.isdigit():
        print("Invalid input! Must be digits and match the length.")
        continue

    attempts += 1

    if feedback(random_number, user_input):
        print("You won!")
        cursor.execute('UPDATE quiziz SET point = point + 1 WHERE user_id = %s;', (user_id,))
        connection.commit()
        break
else:
    print("You lost.")
    cursor.execute('UPDATE quiziz SET defeat = defeat + 1 WHERE user_id = %s;', (user_id,))
    connection.commit()

cursor.close()
connection.close()
