# class variables are shared among all instances of a class
#  defined outside the constructor
#  allow you to share data among all objects from the class

class Student:
    class_year = 2023
    student_number = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_number+=1 

    def student_info(self):
        print(f"Student: {self.name} {self.age} finished {Student.class_year} student number: {Student.student_number}")


student1 = Student("Tom", 22) 
student2 = Student("Rick", 24) 
student3 = Student("Tomas", 32) 
student3 = Student("Morti", 42) 

print(f"Student of :{Student.class_year} ")
student1.student_info()
student2.student_info()
student3.student_info()
