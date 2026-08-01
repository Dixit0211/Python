"""
Inheritances:
type
    1. single Inheritance
    2. Multi-level Inheritance
    3. Multiple Inheritance
"""
#Example of Multi-level Inheritance

class Car:
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")
    
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Diesel")
car1.start()

# Example of Multipal Inheritance

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class c"

c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)