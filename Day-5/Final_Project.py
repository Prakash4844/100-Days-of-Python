# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_level = int(input("Choose Password Level \n1 for Easy\n2 for Hard: "))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
gen_Letter = random.choices(letters, k=nr_letters)
gen_Symbol = random.choices(symbols, k=nr_symbols)
gen_Numbers = random.choices(numbers, k=nr_numbers)

generated_password = gen_Letter+gen_Symbol+gen_Numbers

pass_str = ""
pass_str2 = ""
if nr_level == 1:
    print("Generated Password: ", pass_str.join(generated_password))
elif nr_level == 2:
    random.shuffle(generated_password)
    print("Generated Password: ", pass_str2.join(generated_password))
else:
    print("Couldn't understand your choice! So Here's Both")
    print("Generated Password: ", pass_str.join(generated_password))
    random.shuffle(generated_password)
    print("Generated Password: ", pass_str2.join(generated_password))
