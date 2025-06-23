class vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def info(self):
        return f"Vehicle Name: {self.name}, Color: {self.color}"

    def stop(self):
        return f"{self.name} has stopped."

class car(vehicle):
    def __init__(self, name, color, model):
        super().__init__(name, color)
        self.model = model

    def info(self):
        return f"{super().info()}, Model: {self.model}"

    def drive(self):
        return f"{self.name} is driving."

car = car("Toyota", "Red", "Corolla")
print(car.info())
print(car.drive())
print(car.stop())
