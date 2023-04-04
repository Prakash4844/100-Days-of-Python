print(10/3)  # Float
print(int(10/3))  # Int - Equivalent to 10//3 floor division
print(10//3)  # Int
print(round(10/3))  # Int

print(type(round(10/3))) # Int

print(round(10/3, 4))  # Float

# ------------------------------------

a = 0
a += 1  # a = a + 1
print(a)

a -= 1  # a = a - 1
a *= 15  # a = a * 15
a /= 4  # a = a / 4

print(a)
# ------------------------------------

# F-String
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
