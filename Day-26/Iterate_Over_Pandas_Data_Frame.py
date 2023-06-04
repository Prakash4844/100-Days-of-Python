import pandas as pd

students = {
    "student": ['Alex', 'Dave', 'Asha', 'Michael', 'Arjun', 'Roland', 'Sonali', 'Sagar', 'Zaphkiel'],
    "marks": [90, 89, 78, 67, 66, 45, 45, 87, 94],
}

# Iterate over the dictionary
# for (key, value) in students.items():
#     print(key, value)


# Normal Iterate over the data frame
student_df = pd.DataFrame(students)
# for (key, value) in student_df.items():
#     print(key, value, sep='\n')


# Iterate over the data frame using iteritems()
for (index, row) in student_df.iterrows():
    # print(index, row, sep='\n')
    # print(row['student'], row['marks'], sep='\t')
    if row.student == 'Zaphkiel':
        print(row.student, row.marks, sep='\t')
