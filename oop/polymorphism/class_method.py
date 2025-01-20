# 7:40:00

# class method = allow operations related to the class itself
# take (cls) as the first parameter, which represents the class itself



class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students {cls.count} "
    
    @classmethod
    def get_total_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"average gpa ={cls.total_gpa/ cls.count:.2f}"

student1 = Student("Kolyan",2.1)   
student2 = Student("Kolyan",4.3)   

print(Student.get_count())
print(Student.get_total_gpa())