
#welcoming the costumers
print("\nHello!, Welcome to Siddhu Coffee\n")

#Ask your customer what their name is with the input() function and store that in the variable name.
name = input("\nWhat is your Name?\n ")



if name == "Ben" or name == "Sahil" or name == "Loki": 
    evil_Status = input("Are you evil?\n")
    goodDeed = int(input(" How many good deeds have you done today?\n"))
    if   evil_Status == "Yes" and goodDeed < 4:        
         print("You aren't welcome here " + name + ". Just Get out of here!!")
         exit()  
    else:
     print("Ohh, so you're one of the good " + name + ". Welcome to Siddhu Coffee.\n")
else:
    print("\nHello " + name + ", Thank You so much for Coming.\n")


#Coffee Menu
menu = "Black Coffee, Expresso, Cuppucino, latte, chai"

#Ask the costumer what want to order from the menu. then store it in the variable order.
order = input("\n" + name + ", What are you willing to Order today? Here is our today's Special.\n\n" + menu + "\n")



#puting the price of coffee
if order == "chai":
    price = 15
elif order == "Black Coffee":
    price = 3
elif order == "Expresso":
    price = 9
elif order == "Cuppucino":
    price = 12
elif order == "latte":
    cream = input("Do You want Wipped cream? Yes or No?")
    if cream == "Yes" or cream == "yes":
        price = 20
        print("\n\nThe price of latte with wipped cream is : $" + str(price) + "/item\n")
    else:
        price = 10    
else:
    print("Sorry, we don't have that here.")
    exit()


#It will display the cost of each item 
print("\n\nThe price of " + order + " is : $" + str(price) + "/item\n")

#asking the costumer how many of the item they want to have
quantity = input("How many " + order + " you want to Have?\n")


total_cost = price * int(quantity)


#showing the bill amount and saying your order will come soon
print("Thank you. Here is your Total bill amount: $" + str(total_cost))
print("\nSounds good!! " + name + ", we'll have your " + quantity + " " + order + ". Ready to Serve You.")
