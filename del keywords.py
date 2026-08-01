"""
->Used to delete object properties or object itself.

    del s1.name
    del s1
"""
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Dixit")
print(s1.name)

del s1.name  # this also delete s1.name
print(s1.name) # so this give error 

del s1   # delete s1 objects
print(s1) # so this give error

