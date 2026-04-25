
# Making the inventory
inventory = {
    "guitar": {"price": 399.99, "qty": 20},
    "piano": {"price": 199.99, "qty": 10},
    "drums": {"price": 799.99, "qty": 11},
    "bass": {"price": 499.99, "qty": 17},
}

# Printing the inventory in a formatted way 
def display_inventory():
    print("\n"+"="*40)
    print("            INVENTORY")
    print("="*40)

    print("\nItems in stock: ")
    for instrument, info in inventory.items():
        
        print(f"{'Item: ':<5} {instrument:<10} {'Price: $'} {info['price']:<10} {'Quantity: ':<5} {info['qty']:<3}")

# Calculating the total and printing it

    total_inventory_value = sum(
        item["price"]*float(item["qty"])
        for item in inventory.values()
        )
    print(f"\nThe total inventory value: ${total_inventory_value}")
display_inventory()




# Setting up user-search

item_search = input("\nWhat instrument are you looking for?\n") # Getting the item the customer wants
desired_item = inventory.get(item_search)

if desired_item: # checking if the item is in stock
    print(f"\nITEM FOUND!")
    print(f"Price: ${desired_item['price']}")
    print(f"Qty: {desired_item['qty']}")
else:
    print(f"No instruments found under '{item_search}'. Please try again!")
    print("Exiting Now!")
    exit()

# Setting up user-update
try:
    user_choice = int(input("Would you like to 1. Restock or 2.Make a sale?\n")) #asking the user to input an int to make a choice
    if user_choice ==1:
        print("\n--- Restock ---")
        try:
            new_qty = int(input("How many you are adding: "))
            if new_qty < 0: # we can't restock with a negative number. that's a sale.
                print("Invalid number. Please try again!")
                print("Exiting Now!")
                exit()
            inventory[item_search]['qty'] += new_qty #updating the qty value before displaying the new stock
            print(f"\nSTOCK UPDATED")
            display_inventory()
        except ValueError:
                print("Invalid number. Please try again!")
                print("exiting now")
                exit()
    elif user_choice == 2:
        print("\n--- Sale ---")
        try:
            qty_sold = int(input(f"Please enter the number of {item_search}s sold: "))
            if qty_sold < 0:
                print("Invalid Number. Please try again!")
                print("Exiting Now")
                exit()
            elif qty_sold < inventory[item_search]["qty"]:
                inventory[item_search]["qty"] -= qty_sold
                print(f"\nSTOCK UPDATED")
                display_inventory()
            elif qty_sold == inventory[item_search]["qty"]:
                inventory.pop(item_search)
                print(f"\nSTOCK UPDATED")
                display_inventory()
            else:
                print("Not enough items in stock! Please try again or come back after we restock!")
                print("Exiting Now!")
                exit()
        except ValueError:
            print("Invalid number. Please try again!")
            print("exiting now")
            exit()    

    else:
        print("Invalid number. Please try again!")
        print("exiting now")
        exit()

        
except ValueError:
    print("Invalid choice. Please try again!")
    print("exiting now")
    exit()

# Setting up "low stock" tracker

for instrument, info in inventory.items():
    if info["qty"] <10:
        print(f"ALERT! {instrument} LOW STOCK")


