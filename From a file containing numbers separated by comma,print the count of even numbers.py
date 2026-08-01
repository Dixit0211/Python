with open("sampal.txt","w") as f:
    f.write("1,2,56,4,3,466,12")
    f.close

with open("sampal.txt","r") as f:
    data = f.read() # if you cast whole string into integer then use split methode.
    print(data)
    #first methode for split
    nums = data.split(",") # convert inton list
    print(nums)
    count = 0
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)

# scond methode for split
num = ""
for i in range(len(data)):
    if(data[i] == ","):
        print(int(num))
        num = ""
    else:
        num += data[i]
