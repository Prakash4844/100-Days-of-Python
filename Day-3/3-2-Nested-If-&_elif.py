height = int(input("How Tall are you in cm?"))

if height >= 120:
    print("You can ride the roller-coaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You can't ride the roller-coaster, grow taller! and come back.")

# Note: The elif statement is short for else if. It allows us to check for multiple expressions.
