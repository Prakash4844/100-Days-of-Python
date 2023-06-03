import math

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆
'''You are going to write a List Comprehension to create a new list called squared_numbers. This new list should 
contain every number in the list numbers but each number should be squared.

e.g. `4 * 4 = 16`

4 squared equals 16.

DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.
'''

# Write your 1 line code 👇 below:

squared_numbers = [num**2 for num in numbers]

# Write your code 👆 above:

print(squared_numbers)
