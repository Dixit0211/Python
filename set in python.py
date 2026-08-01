"""
set is the collection of the unordered items.
Each element in the set must be unique & immutable.

nums = {1,2,3,4}
set2 = {1,2,2,2}

#repeated elements stored only once, so it resolved to {1,2}

null_set = set() # empty set syntax

# we are don't store the list and dictionary in the set because it is mutable and the set is immutable.
"""

collection = {1,2,3,4,"hello","world"}

print(collection)
print(type(collection))
print(len(collection)) # total number of items

null_set = set() # empty set because null_set={} for emptydictionary