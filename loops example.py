# print numbers from 1 to 100.

i = 1
while i <= 100:
    print(i)
    i += 1

# print numbers from 100 to 1.

j=100
while j >= 1:
    print(j)
    j -= 1

# print the multiplication table of a number n.

n = int(input("Enter the number:"))
k = 1
while k <= 10:
    print(n,"*",k,"=",k*n)
    k += 1

# print the element of the folloeing list using loop

list = [1,4,9,16,36,49,64,81,100]
l = 0
n = len(list)
while l < n:
    print(list[l])
    l += 1

# SEARCH FOR A NUMBER X IN THIS TUPLES USING LOOP:
# (1,,4,9,16,25,36,49,64,81,100)

tuples = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the number:"))
m = 0
while m < len(tuples):
    if(tuples[m] == x):
        print("number index is",m)
    else:
        print("finding...")
    m += 1

