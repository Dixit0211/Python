# Accessing parts of a string
str = "i am very happy to bing human"

print(str[1:4])
print(str[ :4]) # this print index 0 to 4 
print(str[1: ])# this print index 1 to length of string
print(str[:]) # this print whole string 

#negative indexing

"""
    str = A p p l e
         -5-4-3-2-1 # indexing
         str[-3:-1] is "pl"
"""

str = "Apple"
a = str[-3:-1]
print(a)