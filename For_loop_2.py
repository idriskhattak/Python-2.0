# For Loop

# Problem 1
"""name = 'Idris Khan'

for char in name:
    print(char)
"""
# Problem 2
"""lst = ['Idris','Uneeb','Rumaid']

for el in lst:
    print(el)
    for i in el:
        print(i)"""

# Problem 3
"""n = 5

for i in range(n):
    print(i)"""

# Problem 4
"""for i in range(5):
    print(i)

for i in range(0,5):
    print(i)
"""

"""# Problem 5
for i in range(1,10,2):
    print(i)"""

# Problem 6: Print even and odd in front even odd number (eg: 1 = even, 2 = odd )
"""for i in range(1,11):
    if i%2==0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")"""
        
    
#---------------------------------------------------------------- Basic Level ---------------------------------------------------------#
# Problem 1: Count Specific Elements:
"""Write a for loop to count how many times the number 3 appears in a list numbers = [1, 2, 3, 4, 3, 5, 3]."""
"""
numbers = [1,2,3,4,5,3]

count = 0
for el in numbers:
    if el==3:
        count +=1

print(count)"""

# Problem 2: Print Index and Value:
"""Write a for loop to print both the index and the value of each element in the list colors = ['red', 'blue', 'green']"""

"""colors = ['red','blue','green']

index = 0
for i in colors:
    print(f"{i} at index {index}")
    index +=1"""

# ------------------------------------------------------Intermediate Level----------------------------------------------------------#
# Problem 1: Generate Multiplication Table:
"""Write a for loop to generate and print a multiplication table for numbers."""
"""num = int(input("Enter the number for it's multiplication table :"))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")"""

# Problem 2: Find Maximum in List:
"""Write a for loop to find the maximum value in a list of integers values = [10, 20, 4, 45, 99]."""

"""numbers = [10,20,4,45,99]

max = 0
for el in numbers:
    if el>max:
        max = el
    
print(max)
"""
# Problem 3 :Filter Odd Numbers:
"""Given a list of integers numbers = [2, 3, 5, 7, 8, 10], use a for loop to create a new list containing only the odd numbers."""

"""numbers = [2,3,5,7,8,10]

odd = []

for el in numbers:
    if el % 2 != 0:
        odd.append(el)

print(odd)"""

# Probelm 4 :Sum of Squares:
"""Write a for loop to compute the sum of squares(**) of all integers from 1 to n, where n is a given number."""

n = int(input("Enter the number to compute the squares from 1 to n :"))

for i in range(n+1):
    print(f"The sum of {i} is {i**2}")





