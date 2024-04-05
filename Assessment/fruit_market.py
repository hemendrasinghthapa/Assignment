menu='''
        welcome to fruit market
        1) manager
        2) customer

'''

mmenu='''
        fruit market manager

        1) add fruit stock
        2) view fruit stock
        3) update fruit stock
        4) quit
'''

stockdict={"apple":{'quantity':23,"price":80}}

def addStock():
    fruit_name=input("enter fruit name")
    qty=int(input("enter qty"))
    price=int(input("enter price"))
    stockdict.update({fruit_name:{"quantity":qty,"price":price}})

    print(stockdict)



while True:
    print(menu)
    choice =int(input("select your role : "))
    if choice==1:
        print(mmenu)
        choice=int(input("enter your choice : "))
        if choice==1:
            print("add fruit stock")
            addStock()
            continue
        elif choice==2:
            print("view stock")
            for key,value in stockdict.items():
                print(key,value)
            continue
        elif choice==3:
            print("update fruit stock")

        elif choice==4:
            exit()
    elif choice==2:
        print("customer")
        pass


        

