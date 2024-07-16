#---> Program to find the largest number
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
num3 = int(input("Enter the third number :"))
num4 = int(input("Enter the fourth number :"))

if num1>num2 and num1>num3 and num1>num4:
    print("The first number is the largest :",num1)

elif num2>num3 and num2>num4:
    print("The second number is the largest :",num2)

elif num3>num4:
    print("The third number is the largest :",num3)

else:
    print("The fourth number is the largest :",num4)
