MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 10
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cuppuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0.0
}

is_no = True

def print_resources(resources):
    print("Water: {}ml".format(resources["water"]))
    print("Milk: {}ml".format(resources["milk"]))
    print("Coffee: {}g".format(resources["coffee"]))
    print("Money: ${}".format(resources["profit"]))

def is_resources_sufficient(resources, resources_name, menu):
    if resources[resources_name] < menu[resources_name]:
        print("Sorry there is not enough {}.".format(resources_name))
        return False
    
    return True

def process_coin():
    print("Please insert coins")
    total_money = int(input("How many quarters? : ")) * 0.25
    total_money += int(input("How many dimes?    : ")) * 0.1
    total_money += int(input("How many nickles?  : ")) * 0.05
    total_money += int(input("How many pennies?  : ")) * 0.01

    return total_money

def is_transaction_successful(total_money, menu_cost):
    if total_money < menu_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total_money > menu_cost:
        print("Here is ${:0.2f} dollars in change".format(round(total_money - menu_cost, 2)))
    return True

def make_coffee(drink_name, order_ingredients):
    global resources

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print("Here is your {}. Enjoy!".format(drink_name))

while is_no:
    menu_input = input("What would you like? (espresso/latte/cappuccino): ")

    if menu_input == "off":
        is_no = False
    elif menu_input == "report":
        print_resources(resources)
    elif menu_input in ["espresso", "latte", "cappuccino"]:
        if not is_resources_sufficient(resources, "water", MENU[menu_input]["ingredients"]):
            continue
        elif not is_resources_sufficient(resources, "milk", MENU[menu_input]["ingredients"]):
            continue
        elif not is_resources_sufficient(resources, "coffee", MENU[menu_input]["ingredients"]):
            continue
        else:
            total_money = process_coin()
            if not is_transaction_successful(total_money, MENU[menu_input]["cost"]):
                continue
            resources["profit"] += MENU[menu_input]["cost"]
            make_coffee(menu_input, MENU[menu_input]["ingredients"])

    else:
        print("Wrong input")