# Write a program to count the number of students with the "A" grade in the following tuple

Tuple = ('C','D','A','A','B','B','A')

print(Tuple.count('A')) # ---> 3

# Store the above values in a list and sort them from 'A' to 'D'

# Store the tuple values in a list
grade_list = list(Tuple)

# Sort the list from 'A' to 'D'
grade_list.sort()

print(grade_list) 