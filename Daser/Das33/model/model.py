from connection.db import connection, cursor

def create():
    create_table = '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            telegram_id VARCHAR(100) NOT NULL,
            username VARCHAR(100) NOT NULL,
            create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    '''
    cursor.execute(create_table)
    connection.commit()