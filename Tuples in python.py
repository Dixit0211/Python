# A built-in data type that lets us create immutable sequence of values.

tup = (87,64,33,95,76)  # tup[0],tup[1]..
print(type(tup))
print(tup)
print(tup[3])

# tup[0] = 43  # NOT allowed in python

tup2 = () # Empty tuples
print(tup2)

"""
 if you create singel element tuples you can write tup = (1,)
 if you write the tup = (2) then python think like it is integer 
"""
a = (1,)
print(type(a))
b = (1,2)
print(type(b))