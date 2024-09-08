# Loops are used to repeat instruction

# 1 Print numbers from 1 to 100
"""i = 1
while i<=100: # ---> while loop will iterate until the condition is True
    print(i)
    i +=1

print('Loop Ended')"""

# 2 Print numbers from 100 to 1
"""i = 100
while i>=1:
    print(i)
    i -=1

print('Loop Ended')"""

# 3: print the multiplication table of number n.
"""n = int(input("Enter any number for multiplication table :"))
i = 1

while i<=10:
    print(f"{n} * {i} =",n*i)
    i +=1
print("Table Ended")"""

# 4: Print the elements of the following list using a loop

"""lst = [1,4,9,16,25,36,49,64,81,100]

idx = 0

while idx < len(lst):
    print(lst[idx])
    idx += 1

print("Loop Ended")"""

# 5: Search for a number x in this tuple using loop

"""x = int(input("Enter a number you want searc in given tuple :"))
tpl = (1,4,9,16,25,36,49,64,81,100)

i = 0
while i < len(tpl):
    if tpl[i]==x:
        print("Found at index :",i)
    i += 1"""

# 6: Break : Used to terminate the loop when encountered

"""i = 1
while i<5:
    if i == 4:
        break
    print(i)
    i +=1
print("Loop Breaked")"""

# 7: Continue : terminates execution in the current iteration & continues execution of the loop with next iteration
"""
i = 0
while i <=10:
    if (i==3):
        i+=1  # 3 value will be skipped
        continue
    print(i)
    i+=1"""

# 8: ODD number example for continue statement
"""i = 0
while i <=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1
"""

# 9: WAP to find the sum of first n natural numbers. 
"""n = int(input('Enter the number to find the sum :'))
sum = 0
i = 1

while i<=n:
    sum +=i
    i +=1

print(sum)"""

# 10: WAP to find the factorial of first n numbers.
"""n = int(input("Enter any number :"))
fact = 1
i = 1

while i<=n:
    fact *=i
    i +=1

print(f"Factorial of {n} is :",fact)
"""





