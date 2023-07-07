# File not found error
# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# Key error
# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# IndexError: list index out of range
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# Type error
# TypeError: can only concatenate str (not "int") to str
# text = "abc"
# print(text + 5)

# Handling errors
try:    # try to do this
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:   # if this error occurs
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:   # if this error occurs
    print(f"The key {error_message} does not exist.")
else:   # if no error occurs
    content = file.read()
    print(content)
finally:    # always do this
    # raise TypeError("This is an error that I made up.")
    file.close()
    print("File was closed.")

# Raising errors
# raise TypeError("This is an error that I made up.")
# raise IndexError("This is an error that I made up.")
# raise KeyError("This is an error that I made up.")

# Create your own exception

try:
    height = float(input("Height: "))
    weight = int(input("Weight: "))
    if height > 3:
        raise ValueError("Human height should not be over 3 meters.")
    bmi = weight / height ** 2
except ValueError as error:
    print("Please enter a valid height.")
except ZeroDivisionError as error:
    print("Please enter a valid height and weight.")
else:
    print(bmi)
