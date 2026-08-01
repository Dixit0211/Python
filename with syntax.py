with open("sampal.txt","r") as f:
    data = f.read()
    print(data)

with open("sampal.txt","w") as f:
    f.write("New data")
    f.close()