class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #def __str__(self):
       # return f"Name: {self.name}: Age: {self.age} years old."
    
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})"
        

student = Student("Bob", 28)

print(student)
