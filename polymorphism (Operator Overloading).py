"""
->When the same operator is allowed to have different meaning according to the context.

Operator & Dunder function

a + b  #addition        a__add__(b)
a - b  #substraction    a__sub__(b)
a * b  #multiplication  a__mul____(b)
a / b  #division        a__truediv____(b)
a % b  #mod             a.__mod____(b)
"""
"""
print(1+3) #3
print("Dixit"+"Prajapati")# concatenate
print([1,2,3]+[4,5,6]) #merge
"""

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i +", self.img, "j")
    
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)
    

num1 = Complex(2, 4)
num1.shownumber()

num2 = Complex(8, 4)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()

num3 = num1 - num2
num3.shownumber()