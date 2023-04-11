programming_dictionary = {
    'Bug': "An error in a program that prevents the program from running as expected.",
    'Function': "A piece of code that you can easily call over and over again.",
    }
# Retrieve Item from Dictionary
print(programming_dictionary['Bug'])

# Adding Item in Dictionary
programming_dictionary["Loop"] = "The art of repeating some action over and over again."

print(programming_dictionary)

# Initialize Empty Dict
empty_Dict2 = dict()
empty_dict = {}

print(type(empty_dict))

# Wipe Dict Clean
# programming_dictionary = {}

# Edit Dict
programming_dictionary["Bug"] = "An Error"

print(programming_dictionary["Bug"])

# Looping on Dict
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


