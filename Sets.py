# Sets is the collection unordered items
# Each element in the set must be unique and immutable

SET = {1,3,2,3,'idris','khan',4}
print(SET)

set1 = set() # we can create empty set like this. 'set1 = {}' this will be dictionary
print(set1)

set1.add(1) # remember only elements in the set are immutable other than that we can add and remove elements in set
print(set1)

set1.add(2)
print(set1)

set1.add(2)
print(set1)

set1.add(3) 
print(set1)

set1.remove((3))
print(set1)

# Union ---> combine both set values and return a new set
set2 = {2,3,4}  # ---> set1 = {1,2}
print(set1.union(set2)) # ---> {1,2,3,4}

# Intersection --->  combine common values and return a new set
print(set1.intersection(set2)) # ---> {2}