
from config import config
from database import *


conn = connect_to_sql(config['host'], config['username'], config['password'],
                      config['name_database'])
cursor = conn.cursor()
cursor.execute('SHOW TABLES')
for tb in cursor:
    print(tb)
