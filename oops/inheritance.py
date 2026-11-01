# Parent Class (Base Class)
# A parent class is a class whose properties and methods
# can be inherited by another class.

class Car:

    def __init__(self, brand, model):
        # Constructor: Automatically called when an object is created.
        # self refers to the current object.
        self.brand = brand
        self.model = model

    def fullname(self):
        # Instance method: A function defined inside a class
        # that operates on the object's data.
        return f"{self.brand} {self.model}"


# Child Class (Derived Class)
# ElectricCar inherits the properties and methods of the Car class.
# Syntax: class ChildClass(ParentClass):

class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):

        # super() is used to access the parent class methods.
        # Here, it calls the parent class constructor (__init__).
        # This initializes brand and model inherited from Car.
        super().__init__(brand, model)

        # Child class's own attribute.
        self.battery_size = battery_size


# Creating an object of the child class.
tesla = ElectricCar("Tesla", "Model S", "85kWh")

# Accessing the inherited attribute from the parent class.
print(tesla.model)

# Accessing the inherited method from the parent class.
print(tesla.fullname())

# Accessing the child class's own attribute.
print(tesla.battery_size)