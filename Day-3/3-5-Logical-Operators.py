height = int(input("How Tall are you in cm?"))
bill = 0

if height >= 120:
    print("You can ride the roller-coaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Children ticket is $5")
    elif age <= 18:
        bill = 7
        print("Teenagers ticket is $7")
    elif 45 <= age <= 55:
        print("Your Ticket is on the house.")
    else:
        bill = 12
        print("Adults pay $12")

    want_picture = input("Do you want a picture? Press Y for Yes and N for No:")

    if want_picture == 'Y':
        print(f"Your total bill is ${bill+3}")
    else:
        print(f"Your total bill is ${bill}")
else:
    print("You can't ride the roller-coaster, grow taller! and come back.")
