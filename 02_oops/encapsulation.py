# Encapsulation:
# Encapsulation is the process of wrapping data (attributes)
# and methods into a single class and controlling access to that data.

class Car:

    def __init__(self, brand, model):
        # Private attributes:
        # Double underscore (__) triggers name mangling.
        # These attributes should not be accessed directly from outside the class.
        self.__brand = brand
        self.__model = model

    # Getter method:
    # Used to access private attributes from outside the class.
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    # Setter method:
    # Used to modify the value of a private attribute.
    def set_model(self, model):
        self.__model = model

    # Instance method to return the full car name.
    def fullname(self):
        return f"{self.__brand} {self.__model}"


# Creating an object of the Car class.
tesla = Car("Tesla", "Model S")

# Accessing private attributes using getter methods.
# print(tesla.__brand)  # AttributeError: direct access is not available.

print(tesla.get_brand())
print(tesla.get_model())

# Updating the private model attribute using the setter.
tesla.set_model("Model P")

# Checking the updated value using the getter.
print(tesla.get_model())

print(tesla.fullname())