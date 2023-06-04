import random

names = ['Alex', 'Dave', 'Asha', 'Michael', 'Arjun', 'Roland', 'Sonali', 'Sagar', 'Zaphkiel', 'Raphael',
         'Gabriel', 'Uriel', 'Raguel', 'Remiel', 'Saraqael', 'Ramiel', 'Azrael', 'Haniel', 'Jeremiel',
         'Jophiel', 'Metatron', 'Raziel', 'Sandalphon', 'Zerachiel']

student_scores = {name: random.randint(1, 100) for name in names}

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

print(passed_students)
