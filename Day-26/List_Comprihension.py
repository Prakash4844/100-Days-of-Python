# numbers: list[int] = [1, 2, 3, 4, 5, 6, 8, 5, 6, 658]
#
# new_list = [item * 2 for item in numbers]
#
# print(new_list)

# name = "Zaphkiel"
#
# new_name = [letter for letter in name]
# print(new_name)

# double_range = [item*2 for item in range(1, 5)]
# print(double_range)

names = ['Alex', 'Dave', 'Asha', 'Michael', 'Arjun', 'Roland', 'Sonali', 'Sagar']
new_names = [name.upper() for name in names if len(name) >= 5]

print(new_names)
