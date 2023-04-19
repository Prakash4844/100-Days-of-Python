import Art
import random

print(Art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
elif difficulty == "medium":
    attempts = 7
else:
    print("You didn't choose a valid difficulty, you lose.")
    attempts = 0

game_over = False

while not game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > random_number:
        print("Too high.")
        attempts -= 1
    elif guess < random_number:
        print("Too low.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {random_number}.")
        game_over = True

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        game_over = True

    elif not game_over:
        print("Guess again.")
