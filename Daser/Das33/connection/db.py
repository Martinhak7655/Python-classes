import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="dbgrancum",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()