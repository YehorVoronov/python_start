
# object = a "bundle" of related attributes (variables) and methods (functions)
# phone, car, book, you need class to create many objects
# class = (blueprint) used to design the structere and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    # methods
    def drive(self):
        print("You drive the car")

    def stop(self):
        print(f"You stop the car {self.model}") 

    def describe(self):
        print(f"car model: {self.model}, car year: {self.year}, car color: {self.color}, car for sale: {self.for_sale}")   