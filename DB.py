import sqlite3
def createTable():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER
    )
    ''')
    conn.commit()
    return conn

def insertProduct(conn,Product_name,nbr):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO products (name, quantity)
    VALUES (?, ?)
    ''', (Product_name, nbr))
    conn.commit()

def updateProduct(conn,product,option,value):
    
    cursor = conn.cursor()
    if option=="1":
        cursor.execute('''
        UPDATE products
        SET name = ?
        WHERE name = ?
        ''', (value, product))
    else:
        cursor.execute('''
        UPDATE products
        SET quantity = ?
        WHERE name = ?
        ''', (value, product))
    conn.commit()