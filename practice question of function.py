# WAP to print the length of a list.(list is the parameter)

def len_list(list):
    return len(list)


list2 = list(input("Enter:"))

print(len_list(list2))

# WAP to print the elemets of a list in single line.(list is the parameters)

def list_el(list1):
    for items in list1:
        print(items,end = " ")
    

list1 = ["hello","palanpure","Ahmedabad"]
list_el(list1)
print()

# write to find the fectorial of n.(n is the parameter)

def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n-1)

print(factorial(5))

#Wap to convert USD to Inr 

def rupees(USD):
    INR = 80*USD
    return INR
print(rupees(9))