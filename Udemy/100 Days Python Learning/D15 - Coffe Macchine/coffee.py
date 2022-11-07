from recipe import MENU, resources

# Todo 1: Prompt user by asking the menu and provide the feedback
print("Hello, I'm the coffee maker assistant")
order = int(input('Type 1 to order "Espresso", Type 2 to order "Latte", or type 3 to order "Cappuccino"?\n'))
"""user order feedback"""


def order_feed(order):
    if order == 1:
        return "espresso"
    elif order == 2:
        return "latte"
    elif order == 3:
        return "cappuccino"
    else:
        return "Nothing"
user_order = order_feed(order)

print(f'"{user_order}" will be served in a minute.')

# Todo 2: Check the resources for the used order
booked_res = MENU[user_order]["ingredients"]
def res_used(order):
    for item in booked_res:
        if booked_res[item] > resources[item]:
            print("Sorry your order is out of stock.\nPlease choose another")
            return False
    return True


# Todo 3: Print report for all ingredients to create new order
def cek_res():
    air = resources["water"]
    susu = resources["milk"]
    kopi = resources["coffee"]
    print(f'Your remaining resources are {air}ml of water, {susu}ml of milk, and {kopi}gr of coffee.')
cek_res()

# Todo 4: Process coins (money)
# Todo 5: Check transaction successful for user coins
# Todo 6: Coffee brewing
def brewing(drink_name, ingrendients):
    for item in booked_res:
        resources[item] -= ingrendients[item]


# Todo 8: et cetera
