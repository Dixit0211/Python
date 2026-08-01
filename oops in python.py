"""

-> to map with real world scenarios, we started using objects in code.
-> This is called object oriented programming.
"""

"""
-> Class is a blueprint for creating objects.

# creating class

class student:
    name = "Dixit kumar"

#creating object (instance)

    s1 =student()
    print(s1.name)
"""
class student:
    name = "Dixit kumar"

s1 = student()
print(s1) # print address
print(s1.name)

s2 = student()
print(s2.name)

class car:
    colour = "blue"
    brand = "Mercedes"

car1 = car()
print(car1.colour)
print(car1.brand)