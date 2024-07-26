# Function: A block os statement or code that perform a specific task.

# 1: Write a function to print the length of a list.
"""def len_lst(lst): # parameters
    return len(lst)

list_1 = [0,1,2,3,4]

print(len_lst(list_1))"""  # Arguments

# 2: WAF to print the elements of a list in a single line
"""def elmnts(lst):
    for i in lst:
        print(i,end=' ')

list_1 = [0,1,2,3,4]

elmnts(list_1)"""

# 3: WAF to find the factorial of n.
"""def fact(n):
    fac = 1
    for i in range(1,n+1):
        fac *=i
    print(f'Factorial of {n} is {fac}')

fact(5)"""

# 4: WAF to convert USD to RS
"""def conv(USD):
    print(f"{USD} United States Dollar is equals to :",USD*278.34)

conv(8)"""

# 5: Recusion: A function try to execute itself again and again till base case is TRUE

"""def show(n):
    if(n==0):  # Base Case
        return
    print(n)
    show(n-1)

show(5)"""

# 6: Write a recursive function to calculate the sum of first n natural numbers
def sum(n):
    if(n==0):
        return
    print(n)
    sum(n-1) +1

sum(5)
