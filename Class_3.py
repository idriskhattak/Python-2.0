# Define a base class called Animal
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")

# Define a Dog class that inherits from Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Define a Cat class that inherits from Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Define a function that uses polymorphism
def animal_sound(animal):
    print(animal.make_sound())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the function with different animal types
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
