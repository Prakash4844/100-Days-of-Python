# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places.

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill: $"))
tip = int(input("How much percentage can you tip? "))

tip_amount = tip*100/bill

bill_to_split = int(input("How many people do you want to split the bill between? "))

print(f"Each person will have to pay amount of ${round((bill+tip)/bill_to_split, 2)}")
