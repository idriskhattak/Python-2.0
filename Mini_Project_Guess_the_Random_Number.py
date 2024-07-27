"""
A random number will be generated and user will have to guess the user number, if the user guess the number high computer will suggest
the number is high, if user guess the number low the computer will suggest the number is low, till the user guessed the right number.
"""

import random

while True:
    num = random.randint(1, 10)
    #print(num)  # For testing purposes, you might want to remove this in the final version
    guess = int(input("Enter a number to Guess (between 1 and 10): "))
    
    while True:
        if guess > num:
            guess = int(input("Enter the value again, you have guessed a greater value than the number: "))
        elif guess < num:
            guess = int(input("Enter the value again, you have guessed a lower value than the number: "))
        else:
            print("Congratulations! You have guessed the right number.")
            break

    again = input("Do you want to play again? (yes/no): ").lower()
    if again == 'no':
        break

print("Game Over")





        

