import random 

while True:

    comp = random.choice(["rock","paper","scissor"])
    print(comp)

    human = input("Enter (rock,paper or scissor)").lower()
    
    if comp == 'rock' and human =='paper':
        print("Human Win")
    elif comp == 'rock' and human == 'scissor':
        print("Computer Win")   
    elif comp == 'rock' and human == 'rock':
        print("It's a Draw")

    elif comp == 'paper' and human == 'scissor':
        print("Human Win")
    elif comp == 'paper' and human == 'rock':
        print("Computer Win")
    elif comp == 'paper' and human == 'scissor':
        print("It's a Draw")

    elif comp == 'scissor' and human == 'paper':
        print('Computer Win')
    elif comp == 'scissor' and human == 'rock':
        print('Human Win')
    elif comp == 'scissor' and human == 'scissor':
        print("It's a draw")
    
    again = input("Do you want to play agian (Yes or NO) :").lower()

    if again == 'no':
        break

print("Game Over")
