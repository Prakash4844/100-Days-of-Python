# Write a program that works out whether if a given number is an odd or even number.

given_number = int(input("Enter a number: "))
if given_number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")