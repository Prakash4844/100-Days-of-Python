# Using Absolute Path of a file
with open("/home/zaphkiel/Documents/Github/Python/file.txt", "r") as file:
    print("Absolute Path")
    print(file.read())

# Using Relative Path of a file
with open("../../file.txt", "r") as file:
    print("\nRelative Path")
    print(file.read())
