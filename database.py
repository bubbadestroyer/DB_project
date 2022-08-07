from multiprocessing import connection
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


def get_categories_from_category(category_id):
    sql = '''SELECT id FROM categories WHERE category = %s'''
    cursor.execute(sql, [category_id])
    result = cursor.fetchall()
    return result[0][0]


def get_categories():
    cursor.execute('''SELECT category FROM categories''')
    result = cursor.fetchall()
    lst = []
    for row in result:
        lst.append(row[0])
    return lst


def insert_data(amount, date, category_id):
    sql = '''INSERT INTO costs (amount, date_of_operation, categories_id) VALUES (%s, %s, %s)'''
    data = [amount, date, category_id]
    print(data)
    cursor.execute(sql, data)
    conn.commit()
    return True


def get_columns_name():
    cursor.execute('''SHOW COLUMNS FROM costs''')
    result = cursor.fetchall()
    list = [row[0] for row in result]
    return list


def get_costs():
    cursor.execute('''SELECT * FROM costs''')
    result = cursor.fetchall()
    lst = []
    for row in result:
        lst.append(tuple([str(rows) for rows in row]))
    return lst



def get_sum_amount():
    cursor.execute('''SELECT SUM(amount) FROM costs''')
    result = cursor.fetchall()
    return result[0][0]


conn = connect_to_sql(config['host'], config['username'], config['password'],
                      config['name_database'])
cursor = conn.cursor(buffered=True)


get_sum_amount()