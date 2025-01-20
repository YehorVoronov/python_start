# inheritance = allows a class to inherit attributes and methods from another class
# helps with code reusability and extensibility
# class Child(Parent)

class Animal:
    home_place = "zooHome Location"
    total_animals = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.total_animals += 1
    def eat(self):
        print(f"{self.name} eats total animals: {Animal.total_animals}")
    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
        print("woof!")

class Cat(Animal):
    def speak(self):
        print("meow!")

class Mouse(Animal):
    def speak(self):
        print("squeek!")


dog1= Dog("Bim", 4)
cat1= Cat("Fino", 5)
mouse1= Mouse("Splinter", 1)

dog1.eat()
cat1.eat()
mouse1.eat()

dog1.speak()
cat1.speak()
mouse1.speak()