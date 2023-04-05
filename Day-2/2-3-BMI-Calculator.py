# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = int(weight) / float(height) ** 2
bmi_as_int = round(bmi)
print(bmi_as_int)
