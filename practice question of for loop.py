# print the element of the following list using a loop.

list = [1,4,9,16,25,36,49,64,81,100]

for el in list:
    print(el)

# search for the a number x in this tuples using loop.

tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the number:"))
idx = 0
for val in tuple:
    if(val == x):
        print(val,"is found at index",idx)
    idx += 1