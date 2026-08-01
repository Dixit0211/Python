"""
Create Account class with 2 attributes - balance & account no.
Create methods for debit, crredit & printing the balance.
"""
class Account:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_no = acc_no

    #debit metode
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("Total balance=",self.get_balance())

    #credited methode
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("Total balance=",self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Account(50000,80150100004662)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(30000)

acc2 = Account(800,80150100001945)
print(acc2.balance)
print(acc2.account_no)



