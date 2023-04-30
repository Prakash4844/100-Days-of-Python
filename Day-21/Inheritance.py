class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")


class Frog(Animals):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def jump(self):
        print(f"{self.name} is jumping")


frog = Frog("Froggy", 1, "Green")
frog.eat()
frog.drink()
frog.jump()
print(frog.color)
