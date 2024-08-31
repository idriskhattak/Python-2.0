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


num_1 = int(input("Enter the first number :"))
num_2 = int(input("Enter the second number :"))
num_3 = int(input("Enter the thrid number :"))

print(f"The largest number is {num_1} ") if num_1>num_2 and num_1>num_3 else print(f"The largest number is {num_2}") if num_2>num_3 else print(f"The largest number is {num_3}")