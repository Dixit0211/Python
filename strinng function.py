"""
 str = "I am a coder"
 str.endswith("er") # return true if string ends with substr
 str.capitalize() # capitalizes 1st char
 str.replace(old,new) # replace all occurrences of old with new
 str.find(word) # return 1st index of 1st occurrences 
 str.count("am") #counts the occurrence of substr
"""

str = "i am studying python from youtube chhanel"

print(str.endswith("nel")) # true because string ends with the nel
print(str.endswith("app")) # False because string does not ends with app

print(str.capitalize()) # its capitalize the 1st character of the string
#its create new string estant of the change in the original string

# if you replace character in the string use str.replace(old,new) and also word in this string
print(str.replace("o","i"))
print(str)
print(str.replace("python","java"))

# str.find(character) return 1st index of 1st occurrences
print(str.find("o"))
print(str.find("from"))
print(str.find("Q")) # if word doesnot exists then give -1 value

# str.count("am") counts the occurrence of substr

print(str.count("o"))
print(str.count("from"))