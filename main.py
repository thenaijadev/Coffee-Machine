
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO:Prompt the user to choose the type of drink they would like.
# TODO: Check if resources are sufficient.
report = {}
money = 0
is_active = True


def is_sufficient(choice):
    drink_ingredients = MENU[choice]["ingredients"]
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def update_resources(choice):
    for item in resources:
        drink_ingredients = MENU[choice]["ingredients"]
        resources[item] -= drink_ingredients[item]


def process_coins(choice):
    quarter = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    quarter_dollar = quarter * 0.25
    dime_dollar = dimes * 0.10
    nickel_dollar = nickels * 0.05
    penny_dollar = pennies * 0.01
    dollar = quarter_dollar + penny_dollar + dime_dollar + nickel_dollar

    cost = MENU[choice]["cost"]
    if dollar > cost:
        global money
        money += cost
        my_change = dollar - cost
        return f"Transaction successful, Your change is {my_change}"
    else:
        return "Insufficient money,Refunding now"


while is_active:
    drink = input("What would you like to drink:(Latte/Espresso/Cappuccino)")
    if drink == "report" or drink == "Report":
        for key in resources:
            report[key] = resources[key]
        report["money"] = money
        for key in report:
            print(key, ":", report[key])
    elif drink == "off" or drink == "Off":
        is_active = False
    else:
        if is_sufficient(drink):
            change = process_coins(drink)
            update_resources(drink)
            print(change)
