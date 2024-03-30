# Store the description
__pizza_type_description = """
                   ==Cheese, Sauce and Toppings ratio according to Pizza Type==

Pizza type                Cheese ratio                Sauce ratio                Toppings ratio

Margherita                   50%                         30%                        20%
Vegetarian                   40%                         35%                        25%
Meat Lovers                  45%                         30%                        25%

"""
__pizza_size_description = """
    ==Diameter and Price according to Pizza Type==

Pizza Size                Diameter                Price

Personal                  8 inches                $8
Medium                    12 inches               $12
Family                    16 inches               $18

"""

pizza_type = '' #store pizza type
pizza_size = '' #store pizza size
total_bill = 0 #store total bill
orders = [] # store order info to print at the end

def __get_pizza_type():
    #this function will get the pizza type. my logic is to numbers as input from the user and determine pizza type using the input
    global pizza_type
    print("\n1. Margherita\n2. Vegetarian\n3. Meat Lovers\n4. Description\n")
    print("Input the concern number to proceed: ", end="")
    __indicator = int(input())
    # if __indicator is 1, pizza type will be Margherita
    # if __indicator is 2, pizza type will be Vegetarian
    # if __indicator is 3, pizza type will be Meat Lovers
    # I used conditionals to make that happened
    while __indicator == 4:
        # loop is to take the input recursively, what if the user inputs 4 multiple times!
        print(__pizza_type_description)
        print("Input the concern number to proceed: ", end="")
        __indicator = int(input())
    if __indicator == 1:
        pizza_type = "Margherita"
    if __indicator == 2:
        pizza_type = "Vegetarian"
    if __indicator == 3:
        pizza_type = "Meat Lovers"
    if __indicator > 4:
        #what if wrong input comes!
        print("Invalid input! Enter the correct number Please : ", end="")
        __get_pizza_type()

def __get_pizza_size():
    #it will get the pizza size to determine the price
    global pizza_size
    print("\n1. Personal\n2. Medium\n3. Family\n4. Description\n")
    print("Input the concern number to proceed: ", end="")
    __indicator = int(input())
    # for __indicator is 1, pizza size will be personal
    # for __indicator is 2, pizza size will be medium
    # for __indicator is 3, pizza size will be family
    while __indicator == 4:
        print(__pizza_size_description)
        print("Input the concern number to proceed: ", end="")
        __indicator = int(input())
    if __indicator == 1:
        pizza_size = "Personal"
    if __indicator == 2:
        pizza_size = "Medium"
    if __indicator == 3:
        pizza_size = "Family"
    if __indicator > 4:
        print("Invalid input! Enter the correct number Please : ", end="")
        __get_pizza_size()

def __take_new_order():
    #to change the global variables:
    global total_bill
    global pizza_type
    global pizza_size
    #reset the values first
    pizza_type = ""
    pizza_size = ""
    __bill = 0
    #get pizza type from the user
    print("\nSelect Pizza Type.")
    __get_pizza_type()
    #get the pizza size also!
    print("\nSelect Pizza Size.")
    __get_pizza_size()
    #we need to get the quantity
    print("Quantity: ", end="")
    __qty = int(input())
    #append to orders list
    orders.append(f"{__qty} {pizza_size} {pizza_type} pizza")
    #determine bill
    if pizza_size == "Personal":
        __bill = 8
    if pizza_size == "Medium":
        __bill = 12
    if pizza_size == "Family":
        __bill = 18
    #tell the user what is selected and how much dollar added to total_price
    print(f"\n{pizza_type} {pizza_size} = + ${_bill}")
    total_bill = total_bill + (__bill * __qty)
    #user may add more pizza in the cart!
    print("Do you want to add more order? (yes / NO) : ")
    __ans_ = input()
    #if user's answer is yes, then recall the function
    if __ans_ == "YES" or __ans_ == "Yes" or __ans_ == "Y" or __ans_ == "y" or __ans_ == "yes" :
        __take_new_order()

def __print_bill():
    #print the orders list
    print("\nYou ordered:")
    for i in range(len(orders)):
        print(orders[i])
    #print the bill
    print(f"\nYour total bill is ${total_bill}")

#program starts from here.
print("\nPizzerina Welcomes you.")
__take_new_order()
__print_bill()
