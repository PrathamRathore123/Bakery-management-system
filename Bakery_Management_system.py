def hello_message():
    print("")
    print("\t|=========          /\     |=======  ===========     /\    /\         /\                                                                            ")
    print("\t|                  /  \    |      |       |         /  \  /  \       /  \                                                         ")
    print("\t|        |=====   /    \   |======|       |        /    \/    \     /    \                                                       ")
    print("\t|        |    |  /======\  | \            |       /            \   /======\                                                     ")
    print("\t|=========    | /        \ |  \      =========== /              \ /        \                                                                ")
    print()
    print("\t\t|=====)     /\     |   /  |=====  |====| |======| ")
    print("\t\t|     |    /  \    |  /   |       |    | |        ")
    print("\t\t|=====)   /====\   |_/    |=====  |====| |======| ")
    print("\t\t|     |  /      \  | \    |       |  \          | ")
    print("\t\t|=====) /        \ |  \_  |=====  |   \_ |======| ")
    print()
    print("\t\t( “Sweet moments, freshly baked with love.” )")
    print("Welcome to Garima Bakers!")
    print("We are here to take your order.")
    order()

def order():
    while True:
        option = input("Would you like to order Pastries or Drinks? Enter 'P' for Pastries, 'D' for Drinks, or 'Q' to quit and get your invoice: ").strip().upper()
        if option == 'P':
            pastries()
        elif option == 'D':
            soft_drinks()
        elif option == 'Q':
            print_invoice()
            break
        else:
            print("Invalid option, please try again.")

def pastries():
    available_pastries = {
        "01": ("Croissant", 499),
        "02": ("Danish Pastry", 499),
        "03": ("Eclair", 499),
        "04": ("Turnover", 499)
    }
    print("\t *****************************************")
    print("\t * NO.*   Pastries      *      PRICE      *")
    print("\t *****************************************")
    for key, (pastry, price) in available_pastries.items():
        print(f"\t * {key}  *  {pastry:<13} *       {price}/-     *")
    print("\t *****************************************")
    request = input("Please select your order (enter the number):  ").strip()
    if request in available_pastries:
        print(f"{available_pastries[request][0]} is available.")
        ordered_items.append(available_pastries[request])
    else:
        print(f"{request} is not available.")

def soft_drinks():
    available_drinks = {
        "01": ("Cola", 199),
        "02": ("Juice", 199),
        "03": ("Coffee", 199),
        "04": ("Tea", 199)
    }
    print("Please order your drinks")
    print("\t *****************************************")
    print("\t * NO.*   Drinks        *      PRICE      *")
    print("\t *****************************************")
    for key, (drink, price) in available_drinks.items():
        print(f"\t * {key}  *  {drink:<12} *       {price}/-     *")
    print("\t *****************************************")
    request = input("Enter your drinks (enter the number):  ").strip()
    if request in available_drinks:
        print(f"{available_drinks[request][0]} is available.")
        ordered_items.append(available_drinks[request])
    else:
        print(f"{request} is not available.")

def print_invoice():
    print("\nHere is your invoice:")
    print("\t *****************************************")
    print("\t * Item             *      PRICE      *")
    print("\t *****************************************")
    total = 0
    for item, price in ordered_items:
        print(f"\t * {item:<15} *       {price}/-     *")
        total += price
    print("\t *****************************************")
    print(f"\t * Total            *       {total}/-     *")
    print("\t *****************************************")
    print("Thank you for your order! Enjoy your meal!")

# Initialize the list to keep track of ordered items
ordered_items = []

# Start the order process
hello_message()
