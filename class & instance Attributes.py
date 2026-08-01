"""
Class & Instance Attributes:

    -> Class.attr
    -> obj.attr
"""
class Student:
    college_name = "Poonji ma pvt.ltd"
    name = "xyz"         # when we not pass the value thane this name is return                                                                                                                                                                           
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = Student("karan",97)
print(s1.name,s1.marks)

s2 = Student("karan",97)
print(s2.name,s2.marks)

print(s1.college_name)