"""
When a function calls itself repeatedlty.

# prints n to 1 backwards
    def show(n):
        if(n == 0):  --> base case
            return
        print(n)
        show(n-1)
"""

def show(n):
    if(n == 0):
        return 
    print(n)
    show(n-1)
    print("End")

show(8)

# write recursion code for fectorial

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))