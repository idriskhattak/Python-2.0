"""Private: Private attributes & methods are meant to be used only within the
class and are not accesible outside from the class"""

class Account():
    def __init__(self,account_name,account_pass):
        self.account_name = account_name  #---> Public
        self.__account_pass = account_pass  #---> Private

    def reset(self):
        print(self.__account_pass)
        
person_1 = Account('Idris','khan')

print(person_1.account_name)
# print(person_1.__account_pass) # this line will cause error because we are trying to access a private attribute outside the class

person_1.reset()  # This will print without any errors
