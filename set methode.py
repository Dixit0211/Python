"""
set.add(element)  # adds an element 

set.remove(element)  # removes the element

set.clear() #empties the set

set.pop() # removes a random value

set.union(set2) #combines both set values & returns new

set.intersection(set2) # combines common values & returns new

# set is mutable but set's element are immutable
set --> mutable
set --> element -->immutable
"""

collection = set()

collection.add(1)
collection.add(2) 
collection.add(2) 
collection.add("Dixit")
collection.add((1,2,3,4))
print(collection)

collection.remove(2)
print(collection)

print(collection.pop())
print(collection.pop())

print(len(collection))
print(collection.clear())

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1.intersection(set2))
