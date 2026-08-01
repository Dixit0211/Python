# Dictionary are used to store data values in key:value pairs.
# They are unordered,mutabel (changeble) & don't allow duplicate keys.

info = {
    "Name" : "Dixit",
    "age" : 19,
    "goal" : "Being human",
}
print(info)
print(type(info))
  
print(info["Name"])
print(info["age"])

info["age"] = 98

print(info["age"])

info["surname"] = "Prajapati"

print(info)

# NULL dictionary 

null_dict = {}

print(null_dict)