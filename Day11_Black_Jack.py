import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

funds = 1000

user_list = []
dealer_list = []


def black_jack():

    total_user = 0
    total_dealer = 0
    deal = True

    while deal:
        initial_deal = 2
        for card in range(0, initial_deal):
            user_choice = random.choice(cards)
            dealer_choice = random.choice(cards)

            if total_user <= 21 and total_dealer <= 21:
                user_list.append(user_choice)
                dealer_list.append(dealer_choice)

                print("User Cards : ", user_list)
                print("Dealer Cards : ", dealer_list[0])

                status = input("Hit or Stand ? ")
                if status == "Hit":
                    black_jack()
                else:
                    for final_user in user_list:
                        total_user += final_user

                    for final_dealer in dealer_list:
                        total_dealer += final_dealer

                    if total_dealer > total_user:
                        print("Dealer wins!")
                    else:
                        print("You win!")
            else:
                print("Total User : ", total_user)
                print("Total Dealer : ", total_dealer)
                if total_dealer > total_user:
                    print("Dealer wins!")
                else:
                    print("You win!")
                    deal = False

amount_to_bet = int(input("Enter amount to bet : "))
if funds > amount_to_bet:
    funds -= amount_to_bet
    black_jack()
else:
    print("Insufficient Funds")
