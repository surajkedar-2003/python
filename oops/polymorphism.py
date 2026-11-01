class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):

        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"



tesla = ElectricCar("Tesla", "Model S", "85kWh")

safari = Car("Tata", "Safari")


print(tesla.model)

print(tesla.battery_size)

print(tesla.fuel_type())
print(safari.fuel_type())