# Write a program that checks if a given year is a leap year. A year is a leap year if it is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400.

year = int(input("Enter the year you to check whether it us leap or not :"))

if year%4==0 and year%100!=0 or year%400==0:
    print(f"The given year {year} is leap year")

else:
    print(f"The given year {year} is not a leap year")
