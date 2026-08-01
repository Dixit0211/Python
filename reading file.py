f = open("string.py","r")

data = f.read()
print(data)
print(type(data))

data1 = f.read(10) # they print first 10 character.
print(data1)
print(type(data1))

data2 = f.readline() # print first line and also print one empty extra line
print(data2)

data3 = f.readline() # print second line and this one also print extra line
print(data3)

data4 = f.readline() # print first line and so on
print(data4)

data5 = f.readline() # print second line and so on
print(data5)

#  if you first call f.read() and after call the f.readline() then first exucute f.read() and number of f.readline() fubnction = no. of empty line