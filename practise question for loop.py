# WAP to find the sum of first n numbers.(using while)

n = int(input("Enter the number:"))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print("sum =",sum)

#WAP to find the fibbonaci of first n numbers.(using for)

n = int(input("Enter the number:"))
a = 1
b = 1
sum = 0 
for i in range(n):
    if(i == 0 or i == 1):
      print(a)
    else:
       sum = a + b
       print(sum)
       a = b
       b = sum
#WAP for print the factorial

i = 1
n = int(input("Enter the number:"))
fact = 1
if(n == 0):
   print(fact)
else:
   for i in range(1,n+1):
    fact = fact * i
print(fact)