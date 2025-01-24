import game_data
import random
import art


celebs = game_data.data
ascii_art = art.logo
ascii_vs = art.vs

print(ascii_art)

# print(random_celeb_against)
# print(random_celeb_compare)

for celeb in range(0,50):
    score = 0
    game_on = True
    while game_on:
        random_celeb_compare = random.randint(0, 50)
        random_celeb_against = random.randint(0, 50)

        if random_celeb_compare == random_celeb_against:
            random_celeb_compare = random.randint(0, 50)
            random_celeb_against = random.randint(0, len(celebs))

        name_comp = celebs[random_celeb_compare]["name"]
        profession_compare = celebs[random_celeb_compare]["description"]
        country_compare = celebs[random_celeb_compare]["country"]
        followers_compare = celebs[random_celeb_compare]["follower_count"]

        name_against = celebs[random_celeb_against]["name"]
        profession_against = celebs[random_celeb_against]["description"]
        country_against = celebs[random_celeb_against]["country"]
        followers_against = celebs[random_celeb_against]["follower_count"]
        # print(name," : ", profession, " : ", country)
        print(f"Compare A : {name_comp}, {profession_compare}, {country_compare}")
        print(ascii_vs)
        # print("VS")
        print(f"Against B : {name_against}, {profession_against}, {country_against}")
        user_guess = input("Who has more followers? Type 'A' or 'B': ")
        if user_guess == "A":
            if followers_compare > followers_against:
                print("Correct Guess!!!!")
                score += 1
            else:
                print("Incorrect Guess")
                print(f"Your score is : {score}")
                game_on = False
                print("GAME OVER!!!!!")
                print("\n" * 3)
                break
        else:
            if followers_against > followers_compare:
                print("Correct Guess!!!!")
                score += 1
            else:
                print("Incorrect Guess")
                print(f"Your score is : {score}")
                game_on = False
                print("GAME OVER!!!!!")
                print("\n" * 3)
                break

        print("\n" * 3)
    break

# print(len(celebs))
