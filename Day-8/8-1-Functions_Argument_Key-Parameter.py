# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call to greet() function and run your code.

def greet(name, income, age):
    print(f"Hello my name is {name}")
    print(f"I am {age} years old")
    print(f"i have an annual income of INR {income} LPA")


user_name = input("Whats your name: ")
user_age = input("How old are you: ")
user_income = input("How much do you earn annually: ")

greet(user_name, age=user_age, income=user_income)
