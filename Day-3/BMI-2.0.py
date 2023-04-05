# BMI Calc 2.0

Height = input("enter your height in m: ")
Weight = input("enter your weight in kg: ")

BMI = int(Weight) / float(Height) ** 2
BMI_as_int = round(BMI)
if BMI_as_int < 18.5:
    print(f"Your BMI is {BMI_as_int}kg/m², you are underweight.")
elif BMI_as_int < 25:
    print(f"Your BMI is {BMI_as_int}kg/m², you have normal weight.")
elif BMI_as_int < 30:
    print(f"Your BMI is {BMI_as_int}kg/m², you are slightly overweight.")
elif BMI_as_int < 35:
    print(f"Your BMI is {BMI_as_int}kg/m², you are obese.")
else:
    print(f"Your BMI is {BMI_as_int}kg/m², you are clinically obese.")