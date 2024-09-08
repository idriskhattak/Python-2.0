# For_Loops are used for sequential traversal. For traversing list,string,tuples etc

# 1: Print the elements of the following list using a loop
"""nums = [1,4,9,16,25,36,79,64,81,100]

for i in nums:
    print(i)
"""

# 2: Search for a number x in this tuple using loop:
"""x = int(input('Enter the number you want to search in tup :'))
tup = (1,4,9,16,25,36,79,64,81,100)
idx = 0 

for i in tup:
    if i==x:
        print(f'{i} is found at index {idx}')
        break
    idx +=1
else:
    print("The given number was not found")"""

# 3: Print numbers from 1 to 100 using range
"""for i in range(100):
    print(i+1)"""

# 4: print numbers from 100 to 1 using range
"""for i in range(100,0,-1):
    print(i)"""
 
# 5: Print the multiplication table of a number n using range.
"""n = int(input('Enter any number for multiplication table :'))

for i in range(1,11):
    print(f"{n} * {i} =",n*i)"""

"""# 6: WAP to find the factorial of first n numbers. 
n = int(input("Enter any number :"))
mul = 1

for i in range(1,n+1):
        mul *=i

print(f"Factorial of {n} is :",mul)"""

num = int(input("Enter a number : "))
mul = 1
i = 1
while i<=num:
        print(i)
        mul*=i
        i +=1

print(mul)
        
