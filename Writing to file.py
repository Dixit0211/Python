

f2 = open("sample.txt","w")
f2.close()

f1 = open("sample.txt","a")
f1.write("hii! my name is dixit.")
f1.close()

f1 = open("sample.txt","a")
f1.write("hii! my name is dixit.")
f1.close()

f3 = open("sample.txt","r")
print(f3.read())
f3.close()

f4 = open("sample.txt","r+")
f4.write("abc") # it overwrite the character from starting
print(f4.read()) # it print from cursor to the end
f4.close()

f5 = open("sample.txt","w+")
print(f5.read()) # we use read function in this w+ truncate data
f5.write("abc")
f5.close()
