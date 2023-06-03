"""
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained:

1
2
3

and file2.txt contained:

2
3
4

result = [2, 3]

IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of
a Loop.

"""
# Write Code Below

with open("File1.txt") as f1:
    list_1 = [int(num) for num in f1.readlines()]

with open("File2.txt") as f2:
    list_2 = [int(num) for num in f2.readlines()]

result = [num for num in list_1 if num in list_2]
result.sort()
# Write your code above 👆

print(result)
