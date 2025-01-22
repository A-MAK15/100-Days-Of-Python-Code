import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

num_to_guess = random.randrange(101)

# print(num_to_guess)

hard_attempts = 5
easy_attempts = 10

def guess_game():
    user_guess = int(input("Make a guess : "))
    attempt = difficulty()
    while attempt < 0:
        if user_guess > num_to_guess:
            print("Too high")
            user_guess = input("Guess again : ")
            attempt -= 1

    while attempt < 0:
        if user_guess < num_to_guess:
            print("Too low")
            user_guess = input("Guess again : ")
            attempt -= 1

    if user_guess == num_to_guess:
        print("You got it, Nice work !!!!")


def difficulty():
    attempts = 0
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        attempts = easy_attempts
    else:
        attempts = hard_attempts

    return attempts


