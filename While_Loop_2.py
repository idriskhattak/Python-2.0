
# -------------------------------------------------------------Basic Questions ------------------------------------------------------
# Problem 1: Simple counting:

"""Write a while loop that prints numbers from 1 to 10."""
"""
i = 10
while i<=10:
    print(i)
    i +=1
"""

# Problem 2: Sum of numbers:
"""Write a while loop that calculates the sum of numbers from 1 to 100.
User input with a condition:"""

"""sum_numbers = 0
num = 1

while num <= 100:
    sum_numbers += num
    num += 1

print("The sum of numbers from 1 to 100 is:", sum_numbers)"""

# Peoblem 3:
"""Write a while loop that asks the user for a number and stops if the number is less than 0."""

"""user_input = int(input("Enter a number (enter a negative number to stop): "))

while user_input >= 0:
    print(f"You entered: {user_input}")
    user_input = int(input("Enter a number (enter a negative number to stop): "))

print("You entered a negative number. Program stopped.")
"""

# Problem 4: Guess the number:
"""Write a program where the user must guess a number between 1 and 10. The program should keep asking until the user guesses the correct number."""

# Problem 5: Factorial calculation:
"""Write a while loop that calculates the factorial of a given number."""

# Problem 6: Infinite loop (with user exit):
"""Create an infinite loop using while True that continuously asks the user to enter a word. If the word is "exit", the loop should stop."""


# ----------------------------------------------------------Intermediate Questions:-------------------------------------------------



# Problem 7: Write a program that takes any positive integer and follows these rules:
"""If the number is even, divide it by 2.
If the number is odd, multiply it by 3 and add 1.
Continue until the number becomes 1, and print how many steps it took.
"""
# Problem 8: Input a positive integer from the user
"""number = int(input("Enter a positive integer: "))
steps = 0  # To keep track of the number of steps

# While loop to follow the Collatz Conjecture rules
while number != 1:
    if number % 2 == 0:
        number = number // 2  # If even, divide by 2
    else:
        number = number * 3 + 1  # If odd, multiply by 3 and add 1
    steps += 1  # Increment step counter after each operation

print(f"It took {steps} steps to reach 1.")"""


# Problem 9: Password prompt:
"""Write a while loop that continuously asks for a password until the correct one is entered. After three wrong attempts, the program should lock the user out.
Sum of squares:"""

"""# Set the correct password
correct_password = "mypassword"

# Initialize the number of attempts
attempts = 0
max_attempts = 3

# While loop to keep asking for the password
while attempts < max_attempts:
    # Ask the user to input the password
    entered_password = input("Enter the password: ")

    # Check if the entered password is correct
    if entered_password == correct_password:
        print("Access granted!")
        break  # Exit the loop if the password is correct
    else:
        attempts += 1
        print(f"Incorrect password. You have {max_attempts - attempts} attempt(s) left.")

# If the loop ends and the attempts are exhausted
if attempts == max_attempts:
    print("Too many incorrect attempts. You are locked out.")"""

# Problem 9: Write a while loop that calculates the sum of squares of integers from 1 to n, where n is provided by the user.


"""# Input n from the user
n = int(input("Enter a positive integer n: "))
sum_of_squares = 0
i = 1  # Start from 1

# While loop to calculate the sum of squares
while i <= n:
    sum_of_squares += i ** 2  # Add the square of i to the sum
    i += 1  # Increment i

print(f"The sum of squares from 1 to {n} is:", sum_of_squares)"""
