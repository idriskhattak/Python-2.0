# Lists are mutable, we can stroe different type of data

list = ['idris',24,6]

print(list)
print(type(list))

# Methods of list

list_2 = [4,3,6,8,1]
print(list_2)

list_2[1:3] #---> select only elements from 1 to 3

list_2[1] = 5 #---> 5 will be added at index 1 

list_2.append(7) #---> will add 7 in the end
print(list_2)

list_2.insert(2,9) #---> 9 will be added at 2nd index
print(list_2)

list_2.sort() #---> sort all the element of the list
print(list_2)

list_2.remove(9) #---> 9 will be remove from the list
print(list_2)

list_2.pop(0) #---> the element at index 0 will be removed
print(list_2)


# Tuple are immutable, It have most of the same methods as List have.

tup = ('idris',23,23.5)
print(type(tup))

# Indexing tuple
print(tup[0])
print(tup[0:2])

# Priting the index of the occurance of the something
print(tup.index('idris'))

# Counting total number of occurance
print(tup.count('idris'))


