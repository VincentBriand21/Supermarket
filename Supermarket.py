# Name : Culminating Assignment (Point Of Sale)
# Purpose : To make a point of sale program
# Author : Muhammad Anang Ayman Ramadhana
# Date and time : 11 January 2021
# -----------------------------------------------------------------------------
import random
import csv
from tkinter import*
from tkinter import messagebox

#TODO:
# use tabulate
# use OOP
# Export and import using CSV format
# Make each customer as an object of which there is a shopping cart as a dictionary format
# * Create a main program
# * Cleanup the main program

# This section of code is my Initialization for the variables
# I could make the initialization in one line for line efficiency but
# It's easier to see if it's laid out line by line

# * Class Variables

class Customer(object):
    def __init__(self, name, creditCard, email, loginCode, transactionAmount,totalSpent=0): 
        self.name = name 
        self.creditCard = creditCard 
        self.email = email
        self.loginCode = loginCode
        self.transactionAmount = transactionAmount
        self.totalSpent = totalSpent


items = []
total = 0
total_revenue = 0
login_code = 0
login_type = 0
login_codes = [0]
items_purchased = []
qty_purchased = []
price = []
customer_info = []
cust_id = {}
login_check = 0


# ---------------------------------- Signup ---------------------------------------------
def signup ():
    name = input("Enter your full name : ")
    creditCard = input("Enter your credit card: ")
    while len(creditCard) != 11:
        creditCard = input("Enter a CORRECT 11 digit credit card information: ")
    
    email = input("Enter your email address: ")
    loginCode = random.randint(100000,999999) #! Future Update : Make sure login code is unique
    print(f"Your Login Code: {loginCode}")
    previousTransactionAmount = 0
    a = Customer(name,creditCard,email,loginCode,previousTransactionAmount) # Make a new customer object, then write it to the database

    with open("customers.csv", 'a') as file:
        file.write(f"{name},{creditCard},{email},{loginCode},{previousTransactionAmount}\n")


# --------------------------------- Login Functions --------------------------------
def checkLoginCode(csv_file_path, login_code):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['LoginCode'] == login_code:
                return True
    return False

def login():
    repeat = True
    while repeat  != False:
        loginCode = input("\nEnter Your Login Code: ")

        # * Manager Login
        if loginCode == "M123" : 
            return 2
        
        # * User Login
        if checkLoginCode("customers.csv", loginCode) == True :
            return 1
        else:
            print("\nPlease enter your login code correctly or sign up if you don't have one.")
            print("1. Re-enter\n2. Sign up")
            option = int(input("What do you want to do: "))
            if option == 1:
                pass
            else:
                signup()

def login_page():
    print("\n|---------Ayman's Supermarket----------|")
    option = int(input("1. Login\n2. New Customer\n3. Exit\nEnter : "))
    return option

# --------------------------------- User Program ----------------------------------------
def userProgram():
    pass

# --------------------------------- Manager Program --------------------------------------
def managerProgram():
    pass

# -------------------------------- MAIN PROGRAM -------------------------------------------
def main():
    exit = False
    while exit != True:
        option = login_page()

        if option == 1: # Login
            loginType = login()
            if loginType == 1:
                userProgram()
            elif loginType == 2:
                managerProgram()

        elif option == 2: # Signup
            signup()

        elif option == 3: # Exit
            print("Thank You For Using The Program")
            exit = False
    return

main()

# Old main program
login_page()
items_drinks=[{"name":"Coca Cola", "Quantity": 100,"Price":10},{"name":"Sprite", "Quantity": 100,"Price":9},{"name":"Beer", "Quantity": 100,"Price":12},{"name":"Wine", "Quantity": 100,"Price":40},{"name":"Water", "Quantity": 100,"Price":3},]
items_snack=[{"name":"Oreo", "Quantity": 100,"Price":10},{"name":"Chips", "Quantity": 100,"Price":12},{"name":"Candy", "Quantity": 100,"Price":5},{"name":"Popcorn", "Quantity": 100,"Price":18},{"name":"Lolipop", "Quantity": 100,"Price":12},]
items_meat=[{"name":"Beef", "Quantity": 100,"Price":60},{"name":"Pork", "Quantity": 100,"Price":40},{"name":"Lamb", "Quantity": 100,"Price":50},{"name":"Chicken", "Quantity": 100,"Price":30},{"name":"Vegan Meat", "Quantity": 100,"Price":80},]
items_fruit=[{"name":"Apple", "Quantity": 100,"Price":8},{"name":"Banana", "Quantity": 100,"Price":7},{"name":"Durian", "Quantity": 100,"Price":18},{"name":"Cherry", "Quantity": 100,"Price":18},{"name":"Grape", "Quantity": 100,"Price":13},]
items_vegetable=[{"name":"Carrot", "Quantity": 100,"Price":6},{"name":"Asparagus", "Quantity": 100,"Price":7},{"name":"Cabbage", "Quantity": 100,"Price":4},{"name":"Onion", "Quantity": 100,"Price":6},{"name":"Potato", "Quantity": 100,"Price":9}]
items_list=[items_drinks,items_snack,items_meat,items_fruit,items_vegetable]
items_list1="1. Drinks, 2. Snack, 3. Meat, 4. Fruit, 5. Vegetables"
#Consumer Side
while True:
    # When the user starts the user's interface options would be shown
    # The options are 1. Shopping cart, 2. Purchase Items, 3. Exit
    if login_type == 1:
        print("|----------Welcome to Ayman's Supermarket----------|")
        print('1. Shopping Cart\n2. Purchase items\n3. Exit')
        choice = int(input('Enter the number of your choice : '))

        # SHOPPING CART
        # The program would prompt the name of the food items, the quantity, price per item and the subtotal
        # In a table format
        if choice == 1 :
            print("\n|----------Shopping Cart----------|")
            print(("Ayman's Supermarket"))
            print("%-23s%-8s%-24s%-s" % ("Name of Food Items", "Qty", "Price Per-Item($HKD)", "Sub-Total"))
            for i in range(len(items_purchased)):
                print(
                    "%-23s%-8d%-24d%-d" % (items_purchased[i], qty_purchased[i], price[i], price[i] * qty_purchased[i]))
            print("")

        # PURCHASE ITEMS
        elif choice == 2:
            print('\n|----------Purchase Items----------|')
            print(items_list1) # This line of code prints the categories available for the user to choose
            category = int(input("which category do you want to buy from, Enter Index Number: "))
            # This chunk of code would print the Name, Quantity and Price of the items,
            # Inside the category choosen by the user
            print("%-14s%-18s%-15s"%("Name","Quantity","Price"))
            for i in range (0,6):
                if i == category:
                    for item in items_list[i-1]:
                        print("%-14s%-18s%-15s"% (item["name"],item["Quantity"],item["Price"]))
                    print("")
                    purchase_item = input('which item do you want to purchase? Enter name : ')
                    # This loop is to ensure the user does not enter an integer,
                    # instead they should input the name of the product
                    while purchase_item.isnumeric() == True:
                        print("Please enter the NAME of the product not the number")
                        purchase_item = input('which item do you want to purchase? Enter name : ')
                    # This loop is to ensure that if the user inputted a quantity more than the stock availability
                    # They are able to input another amount without going back to the main user interface
                    repeat_p = True
                    while repeat_p == True:
                        purchase_quantity = int(input("Enter the amount you want to buy: "))
                        # This loop cross reference every item in the designated category
                        for item in items_list[i-1]:
                            if purchase_item.lower() == item['name'].lower():
                                # This chunk of code will run if the item stock is more than
                                # the quantity demanded by the User
                                if item['Quantity'] >= purchase_quantity:
                                    # This section would calculate the total price needed to be paid
                                    # Quantity bought by the consumer
                                    total = item['Price']*purchase_quantity + total
                                    total_revenue =item['Price']*purchase_quantity + total_revenue
                                    price.append(item['Price'])
                                    print('Pay $', total, 'HKD at the cashier.')
                                    item['Quantity'] -= purchase_quantity
                                    items_purchased.append(purchase_item)
                                    qty_purchased.append(purchase_quantity)
                                    repeat_p = False
                                # If the item stock is empty, the program would prompt the user that the item is sold out
                                elif item['Quantity'] == 0:
                                    print('item is sold out.')
                                # If the quantity demanded by the user is more than the stock available,
                                # The program would prompt the maximum amount the user could buy
                                else :
                                    print("Enter an amount lower than", item["Quantity"],"\nYour Purchase is not recorded")

        # EXIT / PAY
        elif choice == 3:
            # This code would prompt the users for the items they've chosen including the quantity, item price and sub total
            print(("\nAyman's Supermarket"))
            print("%-23s%-8s%-24s%-s" % ("Name of Food Items", "Qty", "Price Per-Item($HKD)","Sub-Total"))
            for i in range(len(items_purchased)):
                print("%-23s%-8d%-24d%-d" %(items_purchased[i],qty_purchased[i],price[i],price[i]*qty_purchased[i]))
            print("\nYou have to pay a Grand Total of HKD$" , total,)
            # This section of code is to record the user's purchase and store it into the Customer ID
            # It includes the transaction amount and the items purchased
            for cust_id in customer_info:
                if int(cust_id['login code']) == int(login_code):
                    cust_id["Previous Transaction Amounts"] += total
                    cust_id["Previous Transaction"] = items_purchased
            # This section of code is the GUI asking the user if they wanted to pay now or add another item
            root = Tk()
            root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
            pay = messagebox.askyesno("Question", "Pay Now?")
            root.withdraw()
            root.destroy()
            root.quit()
            if pay == True:
                # If the user chooses to pay, the program would reset the items, quantity purchased by the user
                # And return them into the login page
                root = Tk()
                root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
                messagebox.showinfo("Ayman's Supermarket", "Thank You For Shopping In Ayman's Supermarket!")
                root.withdraw()
                root.destroy()
                root.quit()
                items_purchased,qty_purchased,price=[],[],[]
                total = 0
                login_page()
            else:
                # If they decided to add another item, they would be redirected back the the start of the main program
                login_type = 1

#MANAGER SIDE
    # This chunk of code shows the user different commands they could use and asks for input
    elif login_type == 2:
        repeat = True
        print("|----------List Of Commands----------|\n")
        print("1. Check Customer Data \n2. Change Selling Price \n3. Add Items \n4. Delete Items \n5. Check Revenue \n6. Check Item Popularity \n7. Check Item Availability \n0. Exit")
        manager_choice= int(input("Enter the command you want : "))

        # CHECK CUSTOMER DATA
        # If the user chooses to check the customer data the program would print out the customer information
        # Including the Name, Credit card, email, login code, previous transaction and the total transaction amount
        # The code would print it on table format using string formatting
        if manager_choice == 1:
            print("\n|------------Customer Informations------------|\n")
            print("%-15s%-20s%-25s%-19s%-40s%-s" %
                  ("Name","Credit Card","Email","Login Code","Previous Transaction","Total Transaction Amount"))
            for cust_id in customer_info:
                print("%-15s%-20s%-25s%-19s%-40s%-s" %
                      (cust_id["name"],cust_id["credit card"],cust_id["email"],cust_id["login code"]
                       ,cust_id["Previous Transaction"],cust_id["Previous Transaction Amounts"]))
            print("")

        # CHANGE PRICE
        elif manager_choice == 2:
            change_price_repeat = True
            # This loop is set so that the user does not have to go back to the main user page if
            # They decided to change the price of multiple items
            while change_price_repeat == True:
                print('\n|----------Change Price----------|')
                # This code will show the user the category choices and ask the user for input
                print(items_list1)
                category = int(input("which category do you want to change the price of an item from?: "))
                # It would print the items in a table format
                print("%-14s%-18s%-15s" % ("Name", "Quantity", "Price"))
                for i in range (1,6):
                    if i == category:
                        for item in items_list[i - 1]:
                            print("%-14s%-18s%-15s" % (item["name"], item["Quantity"], item["Price"]))
                        print("")
                        select_item = input('which item do you want to change the price? Enter name : ')
                        # This is the same error checking as previous error checking,
                        # This checks if the input is an integer, if it is, the loop will keep prompting
                        # The user to input the item name instead
                        while select_item.isnumeric() == True:
                            print("Please enter the NAME of the product not the number")
                            select_item = input('which item do you want to change price? Enter name : ')
                        price_change = int(input("Enter the amount you want to change into: "))
                        for item in items_list[i-1]:
                            if select_item.lower() == item['name'].lower():
                                item['Price']=price_change
                # This is the same GUI as before
                root =Tk()
                root.eval('tk::PlaceWindow %s center'%root.winfo_toplevel())
                change_price_repeat = messagebox.askyesno("Question","Is there anything else you want to change price?")
                root.withdraw()
                root.destroy()
                root.quit()

        elif manager_choice == 3:
            add_items_repeat = True
            while add_items_repeat == True:
                print('\n|------------Add items------------|')
                # The program would ask the user to fill a form to input a new item which consists of
                # Item name, Quantity, and price
                print('To add an item fill in the form')
                item = {}
                item['name'] = input('Item name : ')
                # These try and repeat codes is to make sure the inputted value from the user is an integer
                while repeat == True:
                    try:
                        item['Quantity'] = int(input('Item quantity : '))
                        break
                    except ValueError:
                        print('Quantity should only be in integers')
                while repeat == True:
                    try:
                        item['Price'] = int(input('Price $ : '))
                        repeat = False
                    except ValueError:
                        print('Price should only be in integers')
                print('Item has been added.')
                print(items_list1)
                print(item)
                # After finished filling out the form, the program would ask the user about
                # which category should this item be added into
                which_list = int(input("Which category do you want this item to be added into?: "))
                for i in range(len(items_list)+1):
                    if which_list == i:
                        items_list[i-1].append(item)
                items.append(item)
                # The last part is that the program would ask the user if there is anything else to be added
                # If the user says yes, the loop goes on but if the user says no the loop breaks as
                # the while loop repeat condition is changed to false
                root =Tk()
                root.eval('tk::PlaceWindow %s center'%root.winfo_toplevel())
                add_items_repeat = messagebox.askyesno("Question","Is there Any other item you want to add?")
                if add_items_repeat == True:
                    repeat = True
                    root.withdraw()
                    root.destroy()
                    root.quit()
                else:
                    add_items_repeat = False
                    root.withdraw()
                    root.destroy()
                    root.quit()    
        # DELETE ITEMS
        elif manager_choice == 4:
            print('\n|----------Delete Items----------|')
            # This will print out the different category option and ask the user for input
            print(items_list1)
            category = int(input("which category do you want to change the remove an item from: "))
            # It would then print the Item name quantity and price in a table format
            print("%-14s%-18s%-15s" % ("Name", "Quantity", "Price"))
            for i in range(1, 6):
                if i == category:
                    for item in items_list[i - 1]:
                        print("%-14s%-18s%-15s" % (item["name"], item["Quantity"], item["Price"]))
                    print("")
                    # After the item choices are shown, the user can choose which item to delete
                    delete_item = input('which item do you want to delete? Enter Name: ')
                    for item in items_list[i - 1]:
                        if delete_item.lower() == item['name'].lower():
                            items_list[i-1].remove(item)

        # CHECK REVENUE
        elif manager_choice == 5:
            # This code would print out the total revenue
            print("|------------Revenue Data------------|")
            print("Since the profit margin of our product is always 50%")
            print("\n The total money earned before expenses is HKD$", total_revenue)
            print("\nThe current revenue is HKD$", total_revenue / 2,"\n")

        # MOST POPULAR ITEMS
        elif manager_choice == 6:
            # This code would check the most sold items
            print("These are the most popular Items")
            print("%-10s%-5s" % ("Name", "Items Sold"))
            # This loop is used to scroll through all 5 categories
            # It would then see which items are already bought by the users
            # It would then print out the Item name and Quantity in table format
            for i in range (5):
                for item in items_list[i-1]:
                    if 100- item["Quantity"]!= 0:
                        print("%-10s%-5d" % (item["name"],100-item["Quantity"]))
            print("")

        # CHECK ITEM AVAILABILITY
        elif manager_choice == 7:
            print(items_list1)
            category_manager = int(input("which category do you want to check from : "))
            print("%-14s%-18s" % ("Name", "Price"))
            for i in range(1, 6):
                if i == category_manager:
                    # This Loop checks the the category input from the manager
                    # And print the items inside that category
                    for item in items_list[i - 1]:
                        print("%-14s%-18s" % (item["name"], item["Price"]))
                    print("")
                    check_item = input('which item do you want to check? Enter name : ')
                    # This loop cross reference the item inside the items list
                    # And print out the item's quantity in stock
                    for item in items_list[i - 1]:
                        if check_item.lower() == item['name'].lower():
                            print(item['name'],"has", item["Quantity"], "items in stock\n")
        # This chunk of code is an option to return to the login page.
        elif manager_choice == 0:
            login_page()