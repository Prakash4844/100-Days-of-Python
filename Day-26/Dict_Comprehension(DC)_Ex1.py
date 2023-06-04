"""
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word 
in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
Example Output

{
'What': 4,
'is': 2,
'the': 3,
'Airspeed': 8,
'Velocity': 8,
'of': 2,
'an': 2,
'Unladen': 7,
'Swallow?': 8
}
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word: len(word) for word in sentence.split()}

print(result)
