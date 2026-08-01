"""
Property:
-> We use @property decorator on any method in the class to the use the method as a property.
"""
class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
            return (self.phy + self.chem + self.math)/3


std1 = Student(98,89,91)
print(std1.percentage)

std1.phy = 97
print(std1.phy)
# but the percentage not change
"""
def calaPercentage(self):
    self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

std1.calaPrecentage()
print(std1.percentage)   # percentage can change
"""
