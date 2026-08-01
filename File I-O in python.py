"""
Python can be used to perform operations on a file.(read & write data)

Types of all files
    1.Text files : .txt , .docx , .log etc.
    2.Binary Files : .mp4, .mov , .png , .jpeg etc. 

we have to open a file before reading or writing

f = open("file_name","mode")
            |           |
simple.txt <-            -> r : read mode
demo.docx                   w : write mode

data = f.read()
f.close( )
"""
f = open("for loop.py","r")

data = f.read()
print(data)
print(type(data))

f.close()

"""
"r" = open for reading(default)
"w" = open for writing, truncating the file  first
"x" = create a new file and open it for writing
"a" = open for writing, appending to the end of the file if it exists
"b" = binary mode
"t" = text mode(default)
"+" = open a disk file for updating(reading and writing)

"""

 