"""
Range function returns a sequence of numbers,starting form 0 by defua;t, and increments by 1(by default), and stops before a specified number.

range(start?,stop,step?)
"""
# range(5) --> 0,1,2,3,4
print(range(5)) # give output range(0,5) 

# if you print the number then

seq = range(5)

print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
# print(seq[5]) this give the ERROR 

# we can use the for loop for print the number 

for i in seq:
    print(seq[i])

# we can also write the 
for j in range(10): # range(stop) here initialy start is equal to 0
    print(j)

for k in range(2,10): # range(start,stop)
    print(k)

for l in range(1,10,3): # range(start,stop,step) 
    print(l)            # here step meaning the increament if 3 then number increment by 3