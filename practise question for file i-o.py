"""
create a new file "practice.txt" using python.Add the following data in it:
    hi everyone
    we are learning File I/O
    using java
    i like programming in java.
"""
with open("practice.txt","a") as f:
    f.write("hi everyone\n")
    f.close()

with open("practice.txt","a") as f:
    f.write("we are learning File I/O\n")
    f.close()

with open("practice.txt","a") as f:
    f.write("using Java.\n")
    f.close()

with open("practice.txt","a") as f:
    f.write("I like programming in Java.\n")
    f.close()

"WAP that replace all occurrences of'Java' with 'python' in above file."

with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)
    f.close()

"Search if the world 'learning' exists in the file or note"

word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("NOT FOUND")
"WAF to find in which line of the file does the word 'learning' occur first. print -1 if word not found."

def check_word(word):
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")

word = "learning"
check_word(word)

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1


check_for_line()


