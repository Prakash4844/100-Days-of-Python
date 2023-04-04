Name_length = len(input("What is your name: "))
# print("You name has " + Name_length + "Characters")
print(type(Name_length))
# print(f"You name has {Name_length} Characters")  # this works

Name_length = str(Name_length)  # Casting int to str
print(type(Name_length))
print("You name has " + Name_length + " Characters.")

a = float(123)
print(type(a))

print(70.5 + float("111"))
print(type(70.5 + float("111")))

print(str(80) + str(160))
