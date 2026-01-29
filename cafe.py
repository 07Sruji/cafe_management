#PYTHON MINI PROJECT - CAFE MANEGEMENT
# STEP1: Greeting the user
# STEP2: Showing menu {"pizza":50, "salad":30, "burger":100, "pop corn":150}
# STEP3: note the item
# STEP4: Check the item in our menu
#         if Yes: add the cost
#             Ask user for anything else 
#                if Yes: note the second item
#                        Check the item in our menu
#                             calculate total cost & display
#                if No: End order & display cost
#          if No: display error message

menu = {
    "pizza":50, "salad":30, "burger":100, "pop corn":150, "Cold Coffee":50, "Milkshake": 40 ,"Chicken Nuggets":100, "French Fries":50 ,"Brownie":60
    
}
    
print("Welcome to our Coders cafe")
print("pizza:50\n salad:30\n burger:100\n pop corn:150\n Cold Coffee:50\n Milkshake: 40\n Chicken Nuggets:100\n French Fries:50\n Brownie:60")
order_item = input("Enter your item:")  

order_total = 0

if order_item in menu:
   order_total += menu[order_item]
   order = input (" Do you want anything else (Yes/No):")
   if order == "Yes":
        order_item2 = input("Enter your second item:")
        if order_item2 in menu:
            order_total += menu[order_item2]
            print(f'Your order value {order_total}')
   else:         
        print(f'Your order value: {order_total}')
else:
    print(" There is No item")
             