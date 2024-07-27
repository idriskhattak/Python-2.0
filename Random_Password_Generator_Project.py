import random
import string

"""print(string.ascii_letters) # this include all letters capital and small
print(string.digits)           # this include digits from 0-9
print(string.punctuation)      # this include puntuations """


password = ""

for i in range(12): # 12 random will be taken from string to create password

    str = random.choice(string.ascii_letters+string.punctuation+string.digits) # Adding these 3 to create random password
    password +=str # adding each string to password

print("Your random generated password is :",password)
