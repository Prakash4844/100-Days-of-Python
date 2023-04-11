student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grade = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    if student_scores[key] > 90:
        student_grade[key] = "Outstanding"
    elif 80 < student_scores[key] < 90:
        student_grade[key] = "Exceeds Expectations"
    elif 70 < student_scores[key] < 80:
        student_grade[key] = "Acceptable"
    elif student_scores[key] < 70:
        student_grade[key] = "Fail"
    else:
        print("Something went wrong")


# 🚨 Don't change the code below 👇
print(student_grade)
