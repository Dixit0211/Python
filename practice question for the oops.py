"""
Qs.Define a Cercle class to create a circle whith radius r using the constructor.
   Define an Area() method of the class which calculates the area of the circle.
   Define a Perimeter() method of the class which allows you to calculate the perimeter
   of the circle.
"""
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return (22/7) * self.radius ** 2
    
    def Perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.Area())
print(c1.Perimeter())

"""
Qs.Define a Employee class eith attributes role,deparment & salary.this class also showDetails() method.
   create Engineer class that inherits properties from
"""
class Employee:
    def __init__(self,role,deparment,salary):
        self.role = role
        self.deparment = deparment
        self.salary = salary
    
    def showDetail(self):
        print("role =",self.role)
        print("deparment =",self.deparment)
        print("salary =",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",50000)


per1 = Employee("Manager","IT",50000)
per1.showDetail()

eng1 = Engineer("Tony stark",35)
eng1.showDetail()

"""
Qs.Create a class called order which stores item & its price.
   use Dunger function __gt__() convey that:
        order1 > order2 if price of order1 > price of order2
"""

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    
    def __gt__(self,odr2):
        return self.price > odr2.price

odr1 = Order("chips",20)
odr2 = Order("sev",10)

print(odr1 > odr2)