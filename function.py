"""
block of statements that perform a specific task.
it also use for reduce redundancy.

def func_name(param1,param2..):     --> function definition
    # some work
     return val

     fun_name(arg1,arg2..) # function call 
"""
# function defination
def cal_sum(a,b): # a and b are perameters
    return a+b

print(cal_sum(5,39)) # function calls; 5 and 39 are argument
print(cal_sum(9,9))
print(cal_sum(5,99))

"""
function has two type:
    1. built- in data type:
        ex: print(),len(),type(),range()...
    2. user define function

# Assign a default value to parameter, Which is used when no argument is passed.
"""
def cal_multipliction(a, b=1): # none-default argument follow default argument
    print(a*b)
    return a*b

cal_multipliction(7) 