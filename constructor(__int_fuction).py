"""
_ _int_ _function(constructor):

-> All classes have a function called _int_(),which is always executed when the object is being initiated.

#creating class
    class Student:
        def __int__(self,fullname):
            self.name = fullname

#creating objects
    s1 = Student("Karan")
    print(s1.name)

-> *The self parameter is a reference to the current instance of the class,
    and is used to access variables that belongs to the class. 
"""
class Student:

#those constructor is executd  which parameter match with call parameter
    # default constructors
    def __init__(self):
        pass

    # parameterized constructors
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print(self) # self indicate the s1 address
        print("adding new student in database..")

s1 = Student("Karan",97)
print(s1)   # self parameter is refrence to the current instance of the class.
print(s1.name)
print(s1.marks)

s2 = Student("Arjun",98)
print(s2.name) # we store data is also called attributes. 
print(s2.marks)