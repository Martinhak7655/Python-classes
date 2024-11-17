# import psycopg2

# connection = psycopg2.connect(
#     host = "localhost",
#     database = "testpy",
#     user = "postgres",
#     password = "MH2012"
# )

# cursor = connection.cursor()
# create_table = '''
# CREATE TABLE IF NOT EXISTS users(
#     id SERIAL PRIMARY KEY,
#     username VARCHAR(100) NOT NULL,
#     password VARCHAR(100) NOT NULL,
#     create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# '''
# cursor.execute(create_table)
# connection.commit()
# insert = '''
# INSERT INTO users (username, password) VALUES (%s, %s);
# '''
# cursor.execute(insert, ("Martin", "12345678"))
# connection.commit()