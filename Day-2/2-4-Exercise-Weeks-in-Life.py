# 🚨 Don't change the code below 👇
Cur_age = int(input("Enter your current age: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

Year_till_90 = 90 - Cur_age

age_days = 365 * Year_till_90
age_week = 52 * Year_till_90
age_months = 12 * Year_till_90

print(f"You have {age_days} Days, {age_week} Weeks and {age_months} Months left")
