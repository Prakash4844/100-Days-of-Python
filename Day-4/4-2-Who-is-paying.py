import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


bill_payer = random.randint(0, len(names)-1)
print(bill_payer)
print(f"{names[bill_payer]} is going to pay the bill today.")
