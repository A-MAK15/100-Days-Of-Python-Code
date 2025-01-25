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
balance = 100

# print(resources["coffee"])
# TODO 4 : Check Availability of resources - Done

# TODO 1 : Ask user what they want, once action is done, ask again

def user_prompt():
    customer_order = input("What would you like? (espresso/latte/cappuccino): ")
    return customer_order

def report(updated_water, updated_milk, updated_coffee, updated_money):
        print(f"Water: {updated_water} ml")
        print(f"Milk: {updated_milk} ml")
        print(f"Coffee: {updated_coffee} g")
        print(f"Money: ${updated_money} ")

# TODO 5 : Request coins if there are enough resources
def process_coins():
    total = 0

    coin = input("Insert coins (quarter, dimes, nickel, pennies) : ")

    if coin == "quarter":
        coin = 0.25
    elif coin == "dimes":
        coin = 0.10
    elif coin == "nickel":
        coin = 0.05
    elif coin == "pennies":
        coin = 0.01

    total += coin

    return total

def ordering():
    if user_prompt() == "espresso":
        esp_water = espresso["ingredients"]["water"]
        esp_coffee = espresso["ingredients"]["coffee"]
        esp_cost = espresso["cost"]

        new_water = resources["water"] - esp_water
        new_coffee = resources["coffee"] - esp_coffee

        if resources["water"] > esp_water:
            if resources["coffee"] > esp_coffee:
                if esp_cost > process_coins():
                    # report(new_water, new_coffee, new_milk, lat_cost)
                    # return new_water, new_coffee, esp_cost
                    return " "
                else:
                    return "Ops!, Insufficient funds"
            else:
                return "Sorry, there isn't enough Coffee"
        else:
            return "Sorry, there isn't enough Water"

    elif user_prompt() == "latte":
        lat_water = latte["ingredients"]["water"]
        lat_milk = latte["ingredients"]["milk"]
        lat_coffee = latte["ingredients"]["coffee"]
        lat_cost = latte["cost"]

        water = resources["water"] - lat_water
        milk = resources["milk"] - lat_milk
        offee = resources["coffee"] - lat_coffee

        if water > lat_water:
            if coffee > lat_coffee:
                if milk > lat_milk:
                    # return new_water, new_coffee, new_milk, lat_cost
                    if lat_cost > process_coins():
                    # report(new_water, new_coffee, new_milk, lat_cost)
                        return " "
                    else:
                        return "Ops!, Insufficient funds"
                else:
                    return "Sorry, there isn't enough Milk"
            else:
                return "Sorry, there isn't enough Coffee"
        else:
            return "Sorry, there isn't enough Water"

        # if water <= lat_water:
        #     if coffee <= lat_coffee:
        #         if milk <= lat_milk:
        #             return new_water, new_milk, new_coffee
        #         else:
        #             print("Sorry, there isn't enough Milk")
        #     else:
        #         print("Sorry, there isn't enough Coffee")
        # else:
        #     print("Sorry, there isn't enough Water")

    elif user_prompt() == "cappuccino":
        cap_water = cappuccino["ingredients"]["water"]
        cap_coffee = cappuccino["ingredients"]["coffee"]
        cap_milk = cappuccino["ingredients"]["milk"]
        cap_cost = cappuccino["cost"]

        water = resources["water"] - cap_water
        milk = resources["milk"] - cap_milk
        coffee = resources["coffee"] - cap_coffee

        if water > cap_water:
            if coffee > cap_coffee:
                if milk > cap_milk:
                    if transaction(balance, cap_cost) == "Proceed":
                        print(f"Your change is ${balance}")
                        return water, coffee, milk, cap_cost
                        # return " "
                    else:
                        return "Ops!, Insufficient funds"
                else:
                    return "Sorry, there isn't enough Milk"
            else:
                return "Sorry, there isn't enough Coffee"
        else:
            return "Sorry, there isn't enough Water"

    elif user_prompt() == "report":
        report(water, coffee, milk, cost) #find a way to invoke this fucntion


        # if water <= cap_water:
        #     if coffee <= cap_coffee:
        #         if milk <= cap_milk:
        #             return new_water, new_milk, new_coffee
        #         else:
        #             print("Sorry, there isn't enough Milk")
        #     else:
        #         print("Sorry, there isn't enough Coffee")
        # else:
        #     print("Sorry, there isn't enough Water")

# TODO 2 : Turn off the coffee machine - Done
coffee_state = True
# TODO 3 : When report is requested in the prompt, return current resources - Done

while coffee_state:
    print(ordering())
    coffee_state = False

# print(process_coins())

# TODO 6 : Check if the funds received are enough
def transaction(bank, cost):
    if bank > cost:
        bank = bank - cost
        return "Proceed"
# TODO 7 : If transaction successful, as the profit will be displayed in the report on its next request.

# TODO 8 : Return change if too much money was given
# TODO 9 : Update Resources
# TODO 10 : Give user their product, repeat process for next customer
