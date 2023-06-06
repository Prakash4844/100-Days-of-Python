# Args are used to pass a variable number of positional arguments to a function.
def add_all(*args):
    """
    Add individual elements of args with [], and return the sum of all elements
    :param args: tuple
    :return: int
    """
    print("Access individual elements of args with [], as it is a tuple", args[-1], args[-2], args[-3])
    total = 0
    for num in args:
        total += num
    return total


print("First Test with 10 Arguments", add_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), "\n")  # 55
print("Second Test with 11 Arguments", add_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100), "\n")  # 155
print("Third Test with 12 Arguments", add_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000), "\n")  # 1155
print("Fourth Test with 13 Arguments", add_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000),
      "\n")  # 11155


# Kwargs are used to pass a variable number of keyword arguments to a function.
def calculate(n, **kwargs):
    """
    Add and multiply individual elements of kwargs with [] with n, and return the sum of all elements
    :param n: Int
    :param kwargs: Dictionary
    :return: Int
    """
    print("Access individual elements of kwargs with [], as it is a dictionary", kwargs["add"],
          kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print("First Test with 2 Keyword Arguments", calculate(2, add=3, multiply=5), "\n")  # 25
print("Second Test with 2 Keyword Arguments", calculate(4, add=3, multiply=5), "\n")  # 35


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kwargs):
        """
        Initialize the class with the given attributes
        :param kwargs: Dictionary
        """
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R", color="Black", seats=4)
print("My Car is a", my_car.make, my_car.model, "with", my_car.color, "color and", my_car.seats,
      "seats", "\n")

my_car = Car(make="Nissan", model="GT-R", color="Black")
print("My Car is a", my_car.make, my_car.model, "with", my_car.color, "color and", my_car.seats,
      "seats", "\n")

my_car = Car(make="Nissan", model="GT-R")
print("My Car is a", my_car.make, my_car.model, "with", my_car.color, "color and", my_car.seats,
      "seats", "\n")

my_car = Car(make="Nissan")
print("My Car is a", my_car.make, my_car.model, "with", my_car.color, "color and", my_car.seats,
      "seats", "\n")

my_car = Car()
print("My Car is a", my_car.make, my_car.model, "with", my_car.color, "color and", my_car.seats,
      "seats", "\n")
