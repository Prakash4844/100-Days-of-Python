import random
import os.path
import Hangman_art

import requests


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# Getting Random Word from MIT_wordlist.py file, Local Copy can Also be found in Same Path
# if File is not present Send a HTTPS Request using Request package to get file from MIT.edu
def get_list_of_words(path='MIT_wordlist.py'):
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    else:
        response = requests.get(
            'https://www.mit.edu/~ecprice/wordlist.10000',
            timeout=10
        )
        string_of_words = response.content.decode('utf-8')
        list_of_words = string_of_words.splitlines()
        # Caching the file
        file = open('MIT_wordlist.py', 'w')
        for word in list_of_words:
            file.write(word + "\n")
        file.close()
        # caching Done
        return list_of_words


print(Hangman_art.logo)

words = get_list_of_words()
# print(words)  # Show All 10000 words

chosen_word = random.choice(words)
# print(chosen_word)  # 👉️ Random Word from 10000 Words

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess
#  lowercase.

# Testing code
# print(f'Pssst, the solution is {chosen_word}.') # Cheat if you want

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# TODO-4: - Create an empty List called display. For each letter in the chosen_word, add a "_" to
#  'display'. So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_"
#  representing each letter to guess.
display = []
guess_str = ""
word_length = len(chosen_word)
for i in range(0, word_length):
    display.append("_")

print(guess_str.join(display))

# TODO-5: - Loop through each position in the chosen_word; If the letter at that position matches 'guess'
#  then reveal that letter in the display at that position. e.g. If the user guessed "p" and the chosen
#  word was "apple", then display should be ["_", "p", "p", "_", "_"]. i have converted it to string so
#  it shows as _pp__


# TODO-6: - Create a variable called 'lives' to keep track of the number of lives left.
#   Set 'lives' to equal length of chosen word.

lives = 6

while "_" in display:  # guess_str.join(display) == chosen_word:
    guess = input("Guess a Letter: ").lower()

    # for letter in chosen_word:
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(Hangman_art.stages[lives])
            print("Right, You have guess correctly.")

    if guess not in chosen_word:
        print("ooh, Wrong Guess!")
        lives -= 1
        print(Hangman_art.stages[lives])
        if lives == 0:
            print("You Lose!")
            break

    # TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every
    #  other letter replace with "_".
    print(guess_str.join(display))
    if guess_str.join(display) == chosen_word:
        print("You won!")
