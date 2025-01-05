import sqlite3
def createTable():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        quantity INTEGER
    )
    ''')
    conn.commit()
    return conn

def insertProduct(conn,Product_name,nbr):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO products (name, quantity)
        VALUES (?, ?)
        ''', (Product_name, nbr))
        conn.commit()
        print("Product inserted successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Integrity Error: {e}")
    except sqlite3.OperationalError as e:
        print(f"Operational Error: {e}")
    except sqlite3.DatabaseError as e:
        print(f"Database Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

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