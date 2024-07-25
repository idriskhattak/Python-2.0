# Create student class that takes name and marks of 3 subject as arguments in constructor,
# then create a method to print the averge.

class Student():
    
    # Attribute
    def __init__(self,name,urdu,english,math): #---> Constructor
        self.name = name
        self.urdu = urdu
        self.english = english
        self.math = math

    # Method ---> basically methods are functions
    def avg(self):
        print('The average of the students is :',(self.urdu+self.english+self.math)/3)

s1 = Student('Idris',60,80,75)

print(s1.name)

s1.avg()