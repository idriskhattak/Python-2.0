# Conditional Statements
# We will write code about whether we can get addmission in US or not.

gpa = float(input("Enter your gpa:"))

if gpa>=2.5 and gpa<=2.9:
    print("You should improve your grades after that you might get addmission int he US")

elif gpa>=3 and gpa<=4:
    print('Your grades are good you can get addmission in the US')

elif gpa>4:
    print("Please enter gpa from 0 to 4 only")

else:
    print("Your grades are low you can't get addmission in US")