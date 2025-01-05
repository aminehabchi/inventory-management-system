import funcs
import DB
import os
conn=DB.createTable()
def menu():
    os.system('clear')
    print("1 -> Add a new product")
    print("2 -> Update the quantity of existing items")
    print("3 -> Delete an item")
    print("4 -> list items")
    print("5 -> Search Item")
    print("6 -> Clear Inventory")
    print("7 -> Exit")
    option=input("--> ")
    match option:
        case "1":
            funcs.addProduct(conn)
            return   
        case "2":
            funcs.update(conn)
            return 
        case "3":
            funcs.delete(conn)
            return 
        case "4":
            funcs.showAllProducts(conn)
            return 
        case "5":
            funcs.showProducts(conn)
            return 
        case "6":
            # clear()
            funcs.clear(conn)
            return 
        case "7":
            exit(0)
        case _:
            menu()
