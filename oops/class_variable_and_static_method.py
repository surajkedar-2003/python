class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def fullname(self):
        return f"{self.brand} {self.model}"

    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    


class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):

        super().__init__(brand, model)
        self.battery_size = battery_size



tesla = ElectricCar("Tesla", "Model S", "85kWh")

safari = Car("Tata", "Safari")


print(tesla.model)

print(tesla.battery_size)

print(Car.total_car)

print(safari.general_description())
print(Car.general_description())