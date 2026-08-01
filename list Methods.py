list = [2,1,3]

list.append(4) # adds one element at the end [2,1,3,4]
print(list)

print(list.sort())  # sorts in ascending [1,2,3]
print(list) # list.sort() is change in original list return None and then youprint list then print list 

print(list.sort(reverse = True)) # sorts in descending order [3,2,1]
print(list) 

print(list.reverse()) # reverse list  [3,1,2]
print(list)

# list.insert(idx,el) USED FOR THE INSERT THE ELEMENT 

print(list.insert(4,7))
print(list)

list.remove(1) # removes first occurrence of element [2,3,1]
print(list)

list.pop(2) # removes element at idx
print(list)

lists = ['a','d','e','f','c','b']
print(lists.sort())
print(lists)
lists.insert(1,'m')
print(lists)