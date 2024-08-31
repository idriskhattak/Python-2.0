"""Write a Python program that performs the following tasks:



Arithmetic Operations: Calculate the sum, difference, and product of num1 and num2, and display the results.


if-elif-else Statements: Ask the user to enter a number between 1 and 10. 
Check if the number is less than 5, equal to 5, or greater than 5, and print a corresponding message:
If the number is less than 5, print "The number is less than 5."
If the number is equal to 5, print "The number is exactly 5."
If the number is greater than 5, print "The number is greater than 5."

List and Tuple: Create a list of the first 5 even numbers and a tuple of the first 3 odd numbers. 
Print the last even number from the list and the last odd number from the tuple."""

"""
Write a Python program that asks the user to enter three numbers. The program should determine and print the largest of the three numbers.

Example Output:

If the user enters 10, 20, and 15, the program should print: "The largest number is 20."
If the user enters 7, 3, and 9, the program should print: "The largest number is 9."
This question encourages students to practice using multiple if-else statements to compare values.
"""
#problem1
num1=10
num2=20
print(num1+num2)

num1=10
num2=30
print(num1*num2)

num1=50
num2=70
print(num1-num2)


#problem2

num1=int(input("enter a number"))
if num1<5:
    print("the number is less than,",num1)

if num1==5:
    print("the number is equal to 5")

if num1>5:
    print("the number is greater than 5")
    

#problem

lis= ["2","4","6","8","10"] 
print(lis[4])

tuple= 4("1","3","5","7","9")
print(tuple[4])