from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
is_on = True
menu = Menu()

coins = MoneyMachine()



while is_on:
    options =menu.get_items()
    choice = input("What would you like? (espresso/latte/cappuccino/) : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coins.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if coins.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


# drink = Menu()
# drink_choice = drink.find_drink("cappuccino")
# # print(drink_choice.name)
#
# check_resources = CoffeeMaker()
# check_resources.is_resource_sufficient(drink_choice)
#

# cost = coins.process_coins()
#
# payment = coins.make_payment(cost)
# # print(payment)
#
# new_report.make_coffee(drink_choice)
