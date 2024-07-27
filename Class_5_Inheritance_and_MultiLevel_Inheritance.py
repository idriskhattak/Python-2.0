# Inheritance : when a one class e.g(Child class) inherit attributes and methods from other another class e.g(parent class) it is called inheritance
# Types of inheritance : 1) Single Inheritance, 2) Multi Level Inheritance, 3) Multiple Inheritance 
class Car():
    def __init__(self,type):
        self.type = type

    def start(self):
        print('The car started')

    def stop(self):
        print('The car stopped')

class Toyota(Car): # ---> Single level Inheritance
    def __init__(self,brand,type):
        super().__init__(type)   # This is used to inherit attribute from parent class
        self.brand = brand 

class Fortuner(Toyota): # ---> Multi Level Inheritance
    def __init__(self, brand,type,make):
        super().__init__(brand,type)
        self.make = make

car = Fortuner('Toyota','Diesel',2023)

print(car.brand)
car.start()
car.stop()
print(car.make)
print(car.type)

