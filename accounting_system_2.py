
inventory = {
           "phone":    {"price":700,   "quantity":50},
           "keyboards":    {"price":700,   "quantity":50},
           "baterries":{"price": 65, "quantity":100},
           
}

  
account_balance = 25000
price = 0
purchased_items = {}
sold_items = {}
history = []
while True:
    
    
    print("\nWelcome to our Warehouse Accounting System, our options are as follow:) \n")
    print(f"""- balance\n- sales\n- purchase\n- account\n- list
- warehouse\n- review\n- End""")
    option = input("please choose the option from the list above : ").lower()


    if option == "account".lower():

            
            print(f"\nBalance now is : {account_balance} Euro")
            
    
    elif option == "balance".lower():

        print(f"- add\n- substract\n- check balance")
        command = input("please choose the option from the list above : ").lower()
        if  command == "add":
            amount= int(input("amount of money added is : "))
            account_balance += amount
            print(f"Balance now is : {account_balance} Euro")
            history.append(f"added {amount} Euro")
            

        elif command == "substract".lower():
            amount= int(input("amount of money substracted is : "))
            account_balance -= amount
            print(f"Balance now is : {account_balance} Euro")
            history.append(f"substaracted amount is {amount} Euro")
        
        elif command == "check balance".lower():
            print(f"{account_balance}")
            
        else:
            print("\nError! Enter a valid option ")
    
    
    elif option == "sales".lower():      
       
        for k, v in inventory.items():
            print(f"\n{k.capitalize()} :")
            for s, t in v.items():
                print(f"-{s} - {t}")
        sold_items = {}

        item_name = input("what item you're selling: ").lower()
        if item_name in inventory:
            print(item_name)
            print( inventory[item_name]["quantity"])
            price = float(input("Provide price per item: "))
            quantity_sold = int(input("Provide the quantity of items you sold: "))
            if quantity_sold <= inventory[item_name]["quantity"]:
               sold_items[item_name]={"price" :price, "quantity": quantity_sold}
               inventory[item_name]["quantity"] = inventory[item_name]["quantity"] - quantity_sold
               account_balance += quantity_sold * price
               history.append(f"We sold {quantity_sold} {item_name} and we got {quantity_sold * price} Euro for them")
            else:
                print("Not enough quantity in stock")
        

        
        else:
            print("Item not found in our inventory list of items")
        
        
    
    elif option == "purchase".lower():
       
        purchased_items = {}

        item_to_buy = input("Provide item name you looking to buy: ").lower()
        price = float(input("Provide price per item: "))
        quantity_to_buy = int(input("Provide the quantity of items you want to purchase: "))

        purchased_items[item_to_buy] = {"price": price, "quantity" : quantity_to_buy }
        print("purchased Items : ", purchased_items)
        if item_to_buy in inventory :
            
            purchased_items[item_to_buy] = {"price": price, "quantity" : quantity_to_buy }
            inventory[item_to_buy]["quantity"] += quantity_to_buy
            account_balance -= quantity_to_buy * price
            history.append(f"We bought {quantity_to_buy} {item_to_buy} for  {quantity_to_buy * price} Euro")
        else:
            inventory.update(purchased_items )
            account_balance -= quantity_to_buy * price
            history.append(f"We bought {quantity_to_buy} {item_to_buy} for  {quantity_to_buy * price} Euro")
        
       


    elif option == "list".lower():
       
       #print(inventory)
       for k, v in inventory.items():
            print(f"\n{k.capitalize()} :")
            for s, t in v.items():
                print(f"{s} - {t}")
    
    elif option == "warehouse".lower():
        product = input("what product you are looking for ? >")
        if product in inventory:
            print(f"we have {inventory[product]["quantity"]} {product}(s) in store and they cost {inventory[product]["price"]} for each")
        else:
            print(f"sorry no {product} in store at the moment")

    elif option == "review".lower():
        for event in history:
            print (event)


    elif option == "End".lower():
            print("Exiting ...\nbye")
            break

    else:
        print("\n Ooops, Error ! please enter a valid option from the list ")

        