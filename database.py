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


def get_categories_from_category(category_id, table_name):
    cursor.execute(f'''SELECT id 
            FROM {table_name}_categories
            WHERE category = "{category_id}"''')
    result = cursor.fetchall()
    return result[0][0]


def get_categories(table_name):
    cursor.execute(f'''SELECT category 
                   FROM {table_name}_categories''')
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
        WHERE (Table_Name="{table_name}_categories" OR Table_name="{table_name}") and COLUMN_NAME != 'categories_id'
        ORDER BY LENGTH(COLUMN_NAME)''')
    result = cursor.fetchall()
    lst = [row[0] for row in result]
    return lst


def get_table(table_name, category = None):
    if category != None:
        cursor.execute(
        f'''SELECT {table_name}.id, amount, category, date_of_operation  
        FROM {table_name}
        INNER JOIN 
        {table_name}_categories 
        ON {table_name}.categories_id = {table_name}_categories.id
        WHERE category = "{category}" 
        ORDER BY id''')
    else:
        cursor.execute(
            f'''SELECT {table_name}.id, amount, category, date_of_operation  
            FROM {table_name}
            INNER JOIN 
            {table_name}_categories 
            ON {table_name}.categories_id = {table_name}_categories.id 
            ORDER BY id''')
    result = cursor.fetchall()
    lst = []
    for row in result:
        lst.append(tuple([str(rows) for rows in row]))
    print(lst)
    return lst

def search_table(table_name, category):
    cursor.execute(
        f'''SELECT {table_name}.id, amount, category, date_of_operation  
        FROM {table_name}
        INNER JOIN 
        {table_name}_categories 
        ON {table_name}.categories_id = {table_name}_categories.id
        WHERE category = "{category}" 
        ORDER BY id''')
    result = cursor.fetchall()
    print(result)



def get_sum_amount(table_name):
    cursor.execute(f'''SELECT SUM(amount) 
                   FROM {table_name}''')
    result = cursor.fetchall()
    return result[0][0]


def get_most_popular_category(table_name):
    cursor.execute(f'''SELECT category 
                    FROM {table_name} 
                    INNER JOIN {table_name}_categories 
                    ON {table_name}.categories_id = {table_name}_categories.id 
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
                    INNER JOIN {table_name}_categories ON {table_name}.categories_id = {table_name}_categories.id
                    GROUP by category''')
    result = cursor.fetchall()
    value = [row[0] for row in result]
    labels = [row[1] for row in result]
    return value, labels


def delete_data(table_name, id):
    cursor.execute(f'''DELETE FROM {table_name} 
                   WHERE id = {id}''')
    conn.commit()


conn = connect_to_sql(config['host'], config['username'], config['password'],
                      config['name_database'])
cursor = conn.cursor(buffered=True)

