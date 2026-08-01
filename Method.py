"""
-> Methodes sre function that belong to objects.

# creating class

class Student:
    def __init__(self,fullname):
        self.name = fullname

    def hello(self):
        print("hello",self.name)

# creating objects

    s1 = student("karan")
    s1.hello()
"""

class Student:
    college_name = "ABC College"

    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
    
    def wellcome(self):
        print("wellcome student",self.name)
    
    def get_marks(self):
        return self.marks
    
s1 = Student("karan",97)
s1.wellcome()
print(s1.get_marks())
