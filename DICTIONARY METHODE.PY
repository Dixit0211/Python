"""
myDict.keys() #returns all key

myDict.values() #returns all values

myDict.items() #return all (kry,val) pairs as tuples

myDict.get("key") # returns the key according to values

myDict.update(newDict) #inserts the specified items to the dictionary  
"""
student = {
    "name" : "Dixitkumar Prajapati",
    "Subject" : {
        "DS" : 19,
        "DBMS" : 19,
        "DF" : 17,
        "PCE" : 12,
        "P&S" : 30,
    },
    "CGPA" : 8.00,
    "year" : "Second"
}

print(student.keys()) # they returns value in tuples
#if you want key values return in list 
print(list(student.keys()))
print(len(student.keys()))

print(student.values())
print(list(student.values()))
print(len(student.values()))

print(student.items())
print(list(student.items()))
print(len(student.items()))

# we use myDict.get("key") then pass such key not avialable in dictionary then it return None value instand of error 
# so we can use this insted of Dict["key"]
print(student.get("Subject"))

student.update({"city" : "Palanpur"})

new_dict = {"first name":"prajapati","fees":"45,000","father name":"kiranbhai"}
student.update(new_dict)

print(student)