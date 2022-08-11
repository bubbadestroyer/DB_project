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
    sql = '''SELECT id 
            FROM categories 
            WHERE category = %s'''
    cursor.execute(sql, [category_id])
    result = cursor.fetchall()
    return result[0][0]


def get_categories():
    cursor.execute('''SELECT category 
                   FROM categories''')
    result = cursor.fetchall()
    lst = []
    for row in result:
        lst.append(row[0])
    return lst


def insert_data(table_name, amount, date, category_id):
    sql = f'''INSERT INTO {table_name} (amount, date_of_operation, categories_id) 
            VALUES (%s, %s, %s)'''
    data = [amount, date, category_id]
    cursor.execute(sql, data)
    conn.commit()
    return True


def get_columns_name(table_name):
    cursor.execute(f'''SELECT distinct(COLUMN_NAME)  
        FROM information_schema.columns 
        WHERE (Table_Name="categories" OR Table_name="{table_name}") and COLUMN_NAME != 'categories_id'
        ORDER BY LENGTH(COLUMN_NAME)''')
    result = cursor.fetchall()
    lst = [row[0] for row in result]
    return lst


def get_costs(table_name):
    cursor.execute(f'''SELECT {table_name}.id, amount, category, date_of_operation  
        FROM {table_name}
        INNER JOIN 
        categories 
        ON {table_name}.categories_id = categories.id 
        ORDER BY id''')
    result = cursor.fetchall()
    lst = []
    for row in result:
        lst.append(tuple([str(rows) for rows in row]))
    return lst


def get_sum_amount(table_name):
    cursor.execute(f'''SELECT SUM(amount) 
                   FROM {table_name}''')
    result = cursor.fetchall()
    return result[0][0]


def get_most_popular_category(table_name):
    cursor.execute(f'''SELECT category 
                    FROM {table_name} 
                    INNER JOIN categories 
                    ON {table_name}.categories_id = categories.id 
                    GROUP BY categories_id 
                    ORDER BY COUNT(*) DESC 
                    LIMIT 1''')
    result = cursor.fetchall()
    return result[0][0]


def get_avg_amount(table_name):
    cursor.execute(f'''SELECT ROUND(AVG(amount),2) 
                   FROM {table_name}''')
    result = cursor.fetchall()
    return result[0][0]


def get_data_for_diagramm(table_name):
    cursor.execute(f'''SELECT SUM(amount), category 
                    FROM {table_name}
                    INNER JOIN categories ON {table_name}.categories_id = categories.id
                    GROUP by category''')
    result = cursor.fetchall()
    value = [row[0] for row in result]
    labels = [row[1] for row in result]
    return value, labels


conn = connect_to_sql(config['host'], config['username'], config['password'],
                      config['name_database'])
cursor = conn.cursor(buffered=True)
