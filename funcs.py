import DB
import os
import menu
def addProduct(conn):
    os.system('clear')
    Product_name=""
    while Product_name=="" or len(Product_name)>20:
        Product_name=input("Name of the new Product: ")
    
    nbr=0
    while nbr<=0:
        nbr=int(input("Quantity"))
        
    DB.insertProduct(conn,Product_name,nbr)
    menu.menu()
    
def update(conn):
    os.system('clear')
    product=input("Enter name of the Product ")
    print("select what you want to update:")
    print("1 -> Product Name")
    print("2 -> Quantity")
    option=input("")
    while option!="1" and option!="2":
        option=input("wrong input, plaese select 1 or 2: ")
        
    if option=="1":
        value=input("enter new Name: ")
        DB.updateProduct(conn,product,option,value)
    else:
        value=input("enter new Qte: ")
        DB.updateProduct(conn,product,option,value)
    menu.menu()
    
def showAllProducts(conn):
    os.system('clear')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print("--------------------------------")
        print(f"Name-> {product[1]}")
        print(f"Qte-> {product[2]}")
    seccess()

def showProducts(conn):
    os.system('clear')
    name=input("enter name of product that you want to show")
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM products WHERE name=?', (name,))
    products = cursor.fetchall()
    for product in products:
        print("--------------------------------")
        print(f"Name-> {product[1]}")
        print(f"Qte-> {product[2]}")
    
    seccess()
    
    
def seccess():
    option="0"
    while option!="1" and option!="2":
        print("\n1-> Back to menu")
        print("2-> exit")
        option=input()
    if option=="1":
        menu.menu()
    else:
        exit(0)

def delete(conn):
    os.system('clear')
    name=input("enter name of product that you want to delete: ")
    cursor=conn.cursor()
    cursor.execute('DELETE FROM products WHERE name=?', (name,))
    seccess()
    
    
def clear(conn):
    cursor=conn.cursor()
    cursor.execute('DROP TABLE products')
    exit(0)