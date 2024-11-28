import sqlite3
from csv import excel

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

import sqlite3


def get_products_by_store(connection, store_id):
    sql = '''
    SELECT p.title, c.title AS category, p.unit_price, p.stock_quantity
    FROM products p
    JOIN categories c ON p.category_code = c.code
    WHERE p.store_id = ?
    '''

    try:
        cursor = connection.cursor()
        cursor.execute(sql, (store_id,))
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(f"Название продукта: {row[0]}")
                print(f"Категория: {row[1]}")
                print(f"Цена: {row[2]}")
                print(f"Количество на складе: {row[3]}")
                print("-" * 40)
    except sqlite3.Error as e:
        print(f'Error fetching products: {e}')


def main():

    stopper = False

    while stopper != True:
        connection = sqlite3.connect("test.db")
        store_id = int(input("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0: \n"))
        get_products_by_store(connection, store_id)
        connection.close()
        if store_id == 0:
            stopper = True
            print('До свидания')


main()


cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS store (
    store_id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title VARCHAR(250) NOT NULL,
    category_code VARCHAR(2) NOT NULL,
    unit_price FLOAT NOT NULL,
    stock_quantity INTEGER NOT NULL,
    store_id INTEGER NOT NULL,
    FOREIGN KEY (category_code) REFERENCES categories(code),
    FOREIGN KEY (store_id) REFERENCES store(store_id)
)
""")

categories_data = [
    ('FD', 'Food products'),
    ('EL', 'Electronics'),
    ('CL', 'Clothing')
]
cursor.executemany("INSERT OR IGNORE INTO categories (code, title) VALUES (?, ?)", categories_data)

store_data = [
    (1, 'Main Street Store'),
    (2, 'Downtown Store'),
    (3, 'Suburban Store')
]
cursor.executemany("INSERT OR IGNORE INTO store (store_id, title) VALUES (?, ?)", store_data)

products_data = [
    (1, 'Apple', 'FD', 0.5, 200, 1),
    (2, 'Laptop', 'EL', 1500.0, 50, 2),
    (3, 'T-Shirt', 'CL', 20.0, 100, 3),
    (4, 'Orange', 'FD', 0.7, 150, 1),
    (5, 'Smartphone', 'EL', 800.0, 30, 2),
    (6, 'Jeans', 'CL', 50.0, 75, 3)
]
cursor.executemany("""
INSERT OR IGNORE INTO products (id, title, category_code, unit_price, stock_quantity, store_id)
VALUES (?, ?, ?, ?, ?, ?)""", products_data)



conn.commit()
conn.close()






