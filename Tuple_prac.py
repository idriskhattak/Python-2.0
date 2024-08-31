# Write a program to count the number of students with the "A" grade in the following tuple
num = (2,3,4,1,7,8,9)
Tuple = ('C','D','A','A','B','B','A')

print(Tuple.count('A')) # ---> 3

# Store the above values in a list and sort them from 'A' to 'D'

grade_list = list(Tuple) # ---> Converted Tuple to list

grade_list.sort() # ---> Sorted the list from 'A' to 'D'

print(grade_list) 

print(type(list(num.sort())))