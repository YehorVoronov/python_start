# static methods = a method that belong to a class rather than any object from that class (instance)
# usually used for general utility functions

# instance methods = Best for operations on instances of the class (objects)
# static methods = best for utility functions that do not need access to class data
# Class methods = best for class-level data or require access to the class itself

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def get_info(self):
        return f"{self.name} = {self.position}"
        #can be used just with  Employee.is_valid_position(, U need only access a class you don't neet to create obgect
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Kriss", "Manager")
employee2 = Employee("Kim", "Director")
employee3 = Employee("Micky", "CTO")

print(Employee.is_valid_position("Manager"))    
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())