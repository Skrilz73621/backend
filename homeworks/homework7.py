import sqlite3

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


def insert_product(db_name, products):
    sql = '''INSERT INTO products(product_title, price, quantity)
    VALUES(?,?,?)
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
            connection.commit()
    except sqlite3.Error as e:
        print(f'Error inserting employee {e}')


def add_15_products(connection):
    products = [
        ("Беспроводные наушники Pro", 150.50, 10),
        ("Смарт-часы X20", 99.99, 5),
        ("Робот-пылесос CleanBot 3000", 250.00, 20),
        ("Игровая клавиатура HyperKey", 75.75, 15),
        ("Пауэрбанк UltraCharge 20000mAh", 120.00, 8),
        ("Смартфон Galaxy S Ultra", 500.00, 3),
        ("Спортивная бутылка H2O Active", 30.00, 50),
        ("USB-хаб MultiPort 7-в-1", 60.00, 40),
        ("Мышь для геймеров SpeedMouse X", 45.50, 25),
        ("Монитор 4K UltraVision", 300.00, 2),
        ("Защитное стекло для смартфона", 10.00, 100),
        ("Внешний жёсткий диск 2TB", 400.00, 4),
        ("Домашняя камера наблюдения", 200.00, 6),
        ("Умная лампа с Wi-Fi", 500.00, 1),
        ("Профессиональный дрон AirFlyer Pro", 1500.00, 2),
    ]
    for product in products:
        insert_product(db_name, product)


def update_quantity(db_name, id, new_quantity):
    sql = '''
    UPDATE products SET quantity = ? WHERE id = ?
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (new_quantity, id))
            connection.commit()
    except sqlite3.errors as e:
        print(f'Error updating quantity: {e}')


def update_price(db_name, id, new_price):
    sql = '''
    UPDATE products SET price = ? WHERE id = ?
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (new_price, id))
            connection.commit()
    except sqlite3.Error as e:
        print(f'Error updating quantity: {e}')


def select_all(db_name):
    sql = """SELECT * FROM products"""
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f'Error selecting products: {e}')


def select_with_params(db_name, price_limit, quantity_limit):
    sql = """SELECT * FROM products WHERE price < ? AND quantity > ? """
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (price_limit, quantity_limit))
            connection.commit()
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f'Error selecting products with params: {e}')


def search_with_params(db_name, word):
    sql = """SELECT * FROM products WHERE product_title like ? """
    try:
        with sqlite3.connect(db_name) as connection:
            search_template = f'%{word.capitalize()}%'
            cursor = connection.cursor()
            cursor.execute(sql, (search_template,))
            connection.commit()
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f'Error searching products with params: {e}')


sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    product_title  VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL
)
'''

db_name = 'hm.db'


# create_table(db_name, sql_to_create_products_table)
# insert_product(db_name, ('Смартфончик iphone nokia SUltra', 500.0, 3))
# add_15_products(db_name)
# select_with_params(db_name, 100, 10)
# search_with_params(db_name, 'смартфон ')
# select_all(db_name)
# update_price(db_name, 1, 52)
# update_quantity(db_name, 1, 1)
# select_all(db_name)