# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("it is a leap year")
        else:
            print("it isn't a leap year")
    else:
        print("it is a leap year")
else:
    print("it isn't a leap year")


# more info about leap year https://www.youtube.com/watch?v=xX96xng7sAE
# for those who prefer to read, like me:
# https://learn.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
