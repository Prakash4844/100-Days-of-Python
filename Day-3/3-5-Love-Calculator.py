# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

combiString = name1+name2
combiString = combiString.lower()

t = combiString.count("t")
r = combiString.count("r")
u = combiString.count("u")
e = combiString.count("e")

true = t+r+u+e

l = combiString.count("l")
o = combiString.count("o")
v = combiString.count("v")
e = combiString.count("e")

love = l+o+v+e

total_score = int(str(true)+str(love))

if total_score <= 10 or total_score >= 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 <= total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
elif total_score >= 55:
    print(f"Your score is {total_score}, You are good together")
else:
    print(f"your score is {total_score}")
