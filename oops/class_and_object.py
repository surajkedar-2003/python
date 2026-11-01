# Class: A class is a blueprint for creating objects.
# It defines the attributes (data) and methods (behaviour) of objects.
class Car:

    # __init__: A special method automatically called when a new object is created.
    # It initializes the object's attributes with the provided values.
    #
    # Constructor: Commonly, __init__() is called the constructor in Python.
    # Technically, __new__() creates the object, while __init__() initializes it.
    def __init__(self, brand, model):

        # self: Refers to the current object.
        # self.brand and self.model are instance attributes.
        self.brand = brand
        self.model = model

    # Instance method: A function defined inside a class that works with an object.
    def fullname(self):
        return f"{self.brand} {self.model}"


# Object: An instance of a class, created using the class name.
first_car = Car("Toyota", "Corolla")

print(first_car.model)
print(first_car.brand)


print(first_car.fullname())