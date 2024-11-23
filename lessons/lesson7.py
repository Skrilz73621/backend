import sqlite3

from select import select


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
        print(f'Connected to SQLite database: {db_name}')
    except sqlite3.Error as e:
        print(f'Error connecting to SQLite database: {e}')
    return connection


def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
            print(f'Table created successfully')
    except sqlite3.Error as e:
        print(f'Error creating table: {e}')


def insert_employee(db_name, employee):
    sql = '''INSERT INTO employees(full_name, salary, hobby, birth_day, is_marry)
    VALUES(?,?,?,?,?)
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
            connection.commit()
    except sqlite3.Error as e:
        print(f'Error inserting employee {e}')


def update_employee(db_name, employee):
    sql = '''
    UPDATE employees SET salary = ?, is_marry = ? WHERE id = ?
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
            connection.commit()
    except sqlite3.Error as e:
        print(f'Error inserting employee {e}')


def delete_employee(db_name, id):
    sql = '''
    DELETE FROM employees WHERE id = ?
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
    except sqlite3.Error as e:
        print(f'Error inserting employee {e}')


def select_all(db_name):
    sql = '''
    SELECT * FROM employees
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f'Error inserting employee {e}')


sql_to_create_employees_table = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    full_name VARCHAR(200) NOT NULL,
    salary FLOAT(10,2) NOT NULL DEFAULT 0.0,
    hobby TEXT DEFAULT NULL,
    birth_day DATE NOT NULL,
    is_marry BOOL DEFAULT FALSE
)
'''

db_name = 'group_48.db'

# my_connection = create_connection(db_name)
# if my_connection is not None:
#     print(f'Creating connection')
#     # create_table(my_connection, sql_to_create_employees_table)
#     insert_employee(my_connection, ('Nurs Isamnkulov', 2400.5, 'Programming', '2007-09-04', False))
#     my_connection.close()
# insert_employee(db_name, ('Adilet Orozaliev', 1.01, 'Dota2', '2007-08-29', False))
# update_employee(db_name, (2.02, False, 2))
# delete_employee(db_name, 4)

select_all(db_name)