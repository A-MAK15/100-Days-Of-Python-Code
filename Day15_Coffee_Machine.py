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
}

espresso = MENU["espresso"]
latte = MENU["latte"]
cappuccino = MENU["cappuccino"]

water = resources["water"]
coffee = resources["coffee"]
milk = resources["milk"]

# print(resources["coffee"])

# TODO 1 : Ask user what they want, once action is done, ask again


def ordering():
    customer_order = input("What would you like? (espresso/latte/cappuccino): ")
    if customer_order == "espresso":
        esp_water = espresso["ingredients"]["water"]
        esp_coffee = espresso["ingredients"]["coffee"]
        esp_cost = espresso["cost"]

        new_water = resources["water"] - esp_water
        new_coffee = resources["coffee"] - esp_coffee

        if water <= esp_water:
            if coffee <= esp_coffee:
                return new_water, new_coffee
            else:
                print("Sorry, there isn't enough Coffee")
        else:
            print("Sorry, there isn't enough Water")

    elif customer_order == "latte":
        lat_water = latte["ingredients"]["water"]
        lat_milk = latte["ingredients"]["milk"]
        lat_coffee = latte["ingredients"]["coffee"]
        lat_cost = latte["cost"]

        new_water = resources["water"] - lat_water
        new_milk = resources["milk"] - lat_milk
        new_coffee = resources["coffee"] - lat_coffee
        
        if water <= lat_water:
            if coffee <= lat_coffee:
                if milk <= lat_milk:
                    return new_water, new_milk, new_coffee
                else:
                    print("Sorry, there isn't enough Milk")
            else:
                print("Sorry, there isn't enough Coffee")
        else:
            print("Sorry, there isn't enough Water")

    elif customer_order == "cappuccino":
        cap_water = cappuccino["ingredients"]["water"]
        cap_coffee = cappuccino["ingredients"]["coffee"]
        cap_milk = cappuccino["ingredients"]["milk"]
        cap_cost = cappuccino["cost"]

        new_water = resources["water"] - cap_water
        new_milk = resources["milk"] - cap_milk
        new_coffee = resources["coffee"] - cap_coffee
        
        if water <= cap_water:
            if coffee <= cap_coffee:
                if milk <= cap_milk:
                    return new_water, new_milk, new_coffee
                else:
                    print("Sorry, there isn't enough Milk")
            else:
                print("Sorry, there isn't enough Coffee")
        else:
            print("Sorry, there isn't enough Water")

# TODO 2 : Turn off the coffee machine - Done
coffee_state = True
# TODO 3 : When report if requested in the prompt, return current resources - Done
while coffee_state:
    print(ordering())
    coffee_state = False
# TODO 4 : Check Availability of resources - Done

# TODO 5 : Request coins if there are enough resources
# TODO 6 : Check if the funds received are enough
# TODO 7 : If transaction successful, as the profit will be displayed in the report on its next request.
# TODO 8 : Return change if too much money was given
# TODO 9 : Update Resources
# TODO 10 : Give user their product, repeat process for next customer
