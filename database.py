import mysql.connector
from mysql.connector import Error
from config import config

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


def get_columns_name():
    cursor.execute('''SHOW COLUMNS FROM costs''')
    result = cursor.fetchall()
    list = [row[0] for row in result]
    return list

def get_date():
    cursor.execute('''SELECT * FROM costs''')
    result = cursor.fetchall()
    lst = []
    print(result)
    for row in result:
        for rows in row:
            lst.append(str(rows))
    lst = [tuple(lst)]
    return lst
        
        
conn = connect_to_sql(config['host'], config['username'], config['password'],
                      config['name_database'])
cursor = conn.cursor()

get_date()
