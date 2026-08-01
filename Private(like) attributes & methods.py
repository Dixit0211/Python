"""
Conceptual Implementations in python
-> Private attributes & methods are meant to be used only within the class and are not
   accessible from outside the class.
"""
class Person:
    __name = "Dixit prajapati"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 =Person()
print(p1.welcome())
print(p1.__hello()) # this give the error
        

class Account:
    def __init__(self,acc_no,acc_pass):
        self.account_no = acc_no
        self.__account_password = acc_pass # we privet the the password we can access only in calss not outside

    def reset_password(self):
         print(self.__account_password)


acc1= Account(80150100004662,"Dixit@2006")
print(acc1.account_no)
print(acc1.reset_password())
print(acc1.__account_password) # we do not access the account password