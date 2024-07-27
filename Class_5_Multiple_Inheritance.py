class Animal():
    def __init__(self,carnivore):
        self.carnivore = carnivore
    
class Dog():
    def __init__(self,breed):
        self.breed = breed

class GermanShephard(Animal,Dog):  # Multiple Inheritance
    def __init__(self, carnivore, breed):
        Animal.__init__(self, carnivore)
        Dog.__init__(self, breed)

dog = GermanShephard('Yes','German')

print(dog.carnivore)
print(dog.breed)


