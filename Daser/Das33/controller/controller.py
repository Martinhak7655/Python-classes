from connection.db import connection, cursor

def signin(telegram_id):
    select = '''
        SELECT * FROM users WHERE telegram_id = (%s);
    '''
    cursor.execute(select, (telegram_id,))
    connection.commit()
    user = cursor.fetchone()
    if user:
        return True

def signup(telegram_id, username):
    insert = '''
        INSERT INTO users (telegram_id, username) VALUES (%s, %s);
    '''
    cursor.execute(insert, (telegram_id, username,))
    connection.commit()

def popoxum(username, user_id):
    update = '''
        UPDATE users SET username = (%s) WHERE telegram_id = (%s);
    '''
    cursor.execute(update, (username, str(user_id)))
    connection.commit()

def jnjel(telegram_id):
    delete = '''
        DELETE FROM users WHERE telegram_id = (%s);
    '''
    cursor.execute(delete, (str(telegram_id),))
    connection.commit()