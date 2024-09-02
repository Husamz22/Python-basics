a = {
        "name":"Cocacola",
        "code":"CC",
        'price':30
    }

b = {
        "name":"Kofola",
        "code":"KK",
        'price':25
    }

c = {
        "name":"Milkshake",
        "code":"MM",
        'price':60
    }

d = {
        "name":"Tea",
        "code":"TT",
        'price':20
    }

items = [a,b,c,d]
coins = 0
credit = 0

is_quit = False

while is_quit == False:
    print('***************\n')
    print("Welcome To The Vending Machine")
    print(f"Your current credit is: {credit}\n")
    print('***************')
    print("LIST OF DRINKS")
    print('***************\n')
    
    for x in items:
        print(f"{x.get('name')} -- {x.get('price')} -- {x.get('code')}")
        print('***************\n')
    
    order = input("Please enter the code of your drink: ")
    for x in items:
        if order == x.get('code'):
            order = x
            order_price = x.get('price')

            coins = int(input(f"You have selected {x.get('name')} - please insert {x.get('price') - credit} coins: "))
            credit += coins

            while credit < order_price:
                coins = int(input(f"You still need {order_price - credit} coins: "))
                credit += coins
                if credit >= order_price:
                    print("Thank you, please pick up your drink")
                    print('***************\n')
                    credit -= order_price   
                    print(f"Your now have {credit} coins")
                    break
            else:
                print("Thank you, please pick up your drink")
                print('***************\n')
                credit -= order_price
                print(f"Your now have {credit} coins")
    exit = input("Press 'C' if you want to continue: ")
    if exit == 'C':
        is_quit= False
    else:
        is_quit= True
