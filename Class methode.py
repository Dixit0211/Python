"""
-> A class method is bound to the class & receives the class as an implicit first argument.

-> Nota - static methode can't access or modify class state & generally for utility.

class Student:
    @classmethod    #decorator
    def college(cls):
        pass
"""

"""class Person:
    name = "anonymous"

    def changename(self,name):
       self.__class__.name = "Rahul"
       # Person.name = name

p1 = Person()
p1.changename("rahul kumar")
print(p1.name)
print(Person.name)
"""
class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)



