"""
-> Methods that don't use the self parameter(work at class level)

class Student:
    @staticmethod    #decorator
    def college():
        print("ABC College")

-> Decorators allow us to wrap another function in order to extend the behaviour ofhte wrapped function,
   without peramently modifiying it.
"""
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    @staticmethod    # decorator
    def hello():
        print("hello my love")
    
    def average(self):
        return sum(self.marks)/3
    
