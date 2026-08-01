"""
A built-in data type that stores set of values.
it can store elements of different type(integer,float,string,etc.)
"""
marks = [87,64,33,95,76]   # marks[0],marks[1]...

student = ["karan",85,"Delhi"] # student[0],student[1]...

student[0] = "Arjun" # allowed in python

len(student) # return length

marks = [94.4,87.5,95.2,66.2,66.4,45.2]
print(marks)
print(type(marks))
print(marks[0]) #94.4
print(marks[4]) #66.2
#print(marks[6]) # list index out of range

# list_name[string_idx : ending_idx]  ending idx is not included

mark = [87,64,33,95,76]

print(mark[1:4]) # is [64,33,95]
print(mark[ :4]) # is same as mark[0:4]
print(mark[1: ]) # is same as mark[1:len(mark)]
print(mark[-3:-1]) # is [33,95]