import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# funds = 1000

user_card_list = []
computer_card_list = []

user_card_init = random.choice(cards)
computer_cards_init = random.choice(cards)

user_card_list.append(user_card_init)
computer_card_list.append(computer_cards_init)

def end_game():
    game = False
    return game

def deal_cards():
    user_cards = random.choice(cards)
    computer_cards = random.choice(cards)

    user_card_list.append(user_cards)
    computer_card_list.append(computer_cards)

    user_score = 0
    computer_score = 0

    for score in user_card_list:
        user_score += score

    for dealer_score in computer_card_list:
        computer_score += dealer_score

    print("Your cards : ", user_card_list, ", current score is: ", user_score)
    print("Computer first card : ", computer_card_list[0])

    if user_score > 21 or computer_score > 21:
        print("Your cards : ", user_card_list, ", final score is: ", user_score)
        print("Computer final hand is : ", computer_card_list, "final score : ", computer_score)
        if user_score > computer_score:
            print("You win!!!")
        else:
            print("Computer wins!!!")
        end_game()
        user_card_list.clear()
        computer_card_list.clear()

        user_card = random.choice(cards)
        computer_cards = random.choice(cards)

        user_card_list.append(user_card_init)
        computer_card_list.append(computer_cards_init)

def black_jack():
    game = True
    while game:
        play_game = input("Do you want to play a game ? 'Y' or 'N' : ")
        if play_game == "Y":
            deal_cards()
            more_card = input("Type 'Y' to get another card or 'N' to pass : ")
            if more_card == "Y":
                deal_cards()
            else:
                game = False

black_jack()
