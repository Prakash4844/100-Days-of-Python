import Art
import Game_Data
import random
import os

first_Choice = random.choice(Game_Data.data)
score = 0
game_over = False


def follower_compare(first, second):
    """
    Checks followers against user's guess
    and returns who have greater number of followers.
    """
    if first['follower_count'] > second['follower_count']:
        print("First have more follower")
        return 'a'
    elif second['follower_count'] > first['follower_count']:
        print("Second have more follower")
        return 'b'
    else:
        print("Tied")
        return 0


def clear():
    """
    Clears the terminal.
    """
    os.system("clear")


while not game_over:
    print(Art.logo)
    second_Choice = random.choice(Game_Data.data)

    if first_Choice == second_Choice:
        second_Choice = random.choice(Game_Data.data)

    if not score == 0:
        print(f"You're right! Current score: {score}")

    print(f'Compare A: {first_Choice["name"]}, {first_Choice["description"]}, {first_Choice["country"]}')

    print(Art.vs)

    print(f'Against B: {second_Choice["name"]}, {second_Choice["description"]}, {second_Choice["country"]}')

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    who_have_more_follower = follower_compare(first_Choice, second_Choice)

    if user_choice == who_have_more_follower:
        score += 1
        first_Choice = second_Choice
        clear()
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
