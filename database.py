import mysql.connector
from mysql.connector import Error

def connect_to_sql(hostname, username, password, name):
    try:
        connection_db = mysql.connector.connect(host=hostname,
                                                user=username,
                                                passwd=password,
                                                database=name)
        print('Соединение установлено')
    except Error as err:
        print(f'Что-то пошло не так: {err}')
    return connection_db