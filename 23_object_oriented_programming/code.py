class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (90, 90, 80 , 70))

print(student.name)
print(student.grades)
print(student.average_grade())
