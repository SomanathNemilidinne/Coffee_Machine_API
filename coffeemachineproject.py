MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0.0,
}
resources_copy = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
latte_ingredients = MENU["latte"]["ingredients"]
espresso_ingredients = MENU["espresso"]["ingredients"]
cappuccino_ingredients = MENU["cappuccino"]["ingredients"]
latte_cost = MENU["latte"]["cost"]
espresso_cost = MENU["espresso"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]
def coins_calculations():
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    dollars = quarters + dimes + nickels + pennies
    return round(dollars, 2)

def deduction(coffee_ingredients):
    resources["water"] -= coffee_ingredients["water"]
    resources["milk"] -= coffee_ingredients.get("milk", 0)
    resources["coffee"] -= coffee_ingredients["coffee"]

def coffee(coffee_ingredients, coffee_cost):
    for ingredient, amount in coffee_ingredients.items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return
    change = coins_calculations()
    if change < coffee_cost:
        print("Sorry that's not enough money, Money refunded.")
    else:
        resources["money"] += coffee_cost
        if change > coffee_cost:
            return_change = change - coffee_cost
            print(f"Here is ${round(return_change, 2)} dollars in change.")
        deduction(coffee_ingredients)
        print(f"Here is your {user_input}☕. Enjoy!")

next_customer = True
while next_customer:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif user_input == "off":
        next_customer = False
    elif user_input == "latte":
        coffee(latte_ingredients, latte_cost)
    elif user_input == "espresso":
        coffee(espresso_ingredients, espresso_cost)
    elif user_input == "cappuccino":
        coffee(cappuccino_ingredients, cappuccino_cost)
    else:
        print("Wrong input, DUMBO!")
