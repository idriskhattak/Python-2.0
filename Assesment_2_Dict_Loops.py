# Problem 1:
"""For Loops:
Finding Common Elements:

Question: Given two lists, list1 = [1, 2, 3, 4, 5] and list2 = [4, 5, 6, 7, 8], write a program using a for loop to 
find and print the common elements between the two lists."""

# Problem 2. Finding Both the Highest and Lowest Grades:
"""You have a dictionary named students where each key is a student's name and the value is another dictionary with keys "age" 
and "grade, Write a program to Find Both the Highest and Lowest Grades:"""

# Problem 3:
"""Question: Write a program that continuously prompts the user to enter a password that is at least 8 characters long. Use a while loop to validate the input. 
If the password is shorter than 8 characters,display an error message and prompt the user again until a valid password is entered."""

# Problem 4: 
""" Write a program that continously prompts the user to check the password if the password is correct or not"""

# Problem 5:
"""Nested Dictionary and Iteration:

Question: You have a dictionary named students where each key is a student's name and the value is another dictionary with keys "age" 
and "grade". Write a program to find and print the name of the student with the highest grade."""

                        # ================================================================================= #


# Problem 1:

"""For Loops:
Finding Common Elements:

Question: Given two lists, list1 = [1, 2, 3, 4, 5] and list2 = [4, 5, 6, 7, 8], write a program using a for loop to 
find and print the common elements between the two lists."""

"""
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
list = []
for el in list1:
    if el in list2:
        list.append(el)

print(list)
"""

# Problem 2. Finding Both the Highest and Lowest Grades:
"""You have a dictionary named students where each key is a student's name and the value is another dictionary with keys "age" 
and "grade, Write a program to Find Both the Highest and Lowest Grades:"""

"""students = {'uneeb':{'age':23,
                     'marks':85},
            'rumaid':{'age':20,
                      'marks':90},
            'idris':{'age':24,
                     'marks':70}}

highest_grade = 0
lowest_grade = 0
top_student = ""
low_student = ""

for student,info in students.items():
    if info["marks"]>highest_grade:
        highest_grade = info["marks"]
        top_student = student

    if info['marks']<highest_grade:
        lowest_grade = info['marks']
        low_student = student

print(top_student)
print(low_student)"""


# Problem 3:
"""Question: Write a program that continuously prompts the user to enter a password that is at least 8 characters long. Use a while loop to validate the input. 
If the password is shorter than 8 characters,display an error message and prompt the user again until a valid password is entered."""

"""password = input("Enter the password for atleast 8 characters :")

while len(password)<=8:
    password = input("Please enter the password the password with atleast 8 characters :")

print(password)
"""
"""password = "idris"
user_pass = input("Enter the password :")

while user_pass!=password:
    user_pass = input("Please enter the correct password :")

print("Password Correct")"""


















"""# Problem 4:
students = {'uneeb':{'age':23,
                     'marks':85},
            'rumaid':{'age':20,
                      'marks':90},
            'idris':{'age':24,
                     'marks':70}}

# print(students['idris']['age'])
max_marks = 0
top_student = " "
for student, info in students.items():
    if info["marks"]>max_marks:
        max_marks = info["marks"]
        top_student = student
    #print(info['marks'])
print(top_student)"""
