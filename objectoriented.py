class Mammal:
    species = "mammal"

    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def description(self):
        return f"{self.name} is a {self.type} and is {self.age} years old."

class Cat(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age, "cat")

class Dog(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age, "dog")


thor = Cat("Thor", 7)
steve = Cat("Steve", 5)
paul = Dog("Paul", 9)



print(thor.description())
print(steve.description())
print(paul.description())













def main():
    thor = Pet("Thor")
    nelson = CuddlyPet("Nelson")

    print(thor.happiness)
    nelson.cuddle(thor)
    print(thor.happiness)
