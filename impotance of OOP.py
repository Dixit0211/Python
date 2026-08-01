"""
Abstraction:
-> Hiding the implementation details of a class and showing the essential features to the user.

Encapsulation:
->Wrapping data and functions into a single unit(objects).
"""

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started..")

car1 = Car()
car1.start()

"""
Inheritance:
->When one class(child/derived) derives the properties & methods of another class(parent/base).

    class Car:
        ...
    
    class ToyotaCar(Car):
        ...

-> in the simpal word we passing some information one class to another class.

types of Inheritance:
1. Single Inheritance : in this single parent class and single child class
2. Multi-level Inheritance : 
3. Multiple Inheritance
"""
class Car1:
    colour = "black"
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")
    
class ToyotaCar(Car1):
    def __init__(self,name):
        self.name = name
    
car3 = ToyotaCar("fortuner")
car4 = ToyotaCar("Land cuiser")

print(car3.name)
print(car4.name)
print(car3.start())
print(car3.colour)