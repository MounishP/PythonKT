class Vehicle:
    def __init__(self, engine, wheels, fuelTank, light, seats):
        self.engine = engine
        self.wheels = wheels
        self.fuel = fuelTank
        self.light = light
        self.seats = seats

    def printVehicle(self):
        print(self.engine, " ", self.wheels, " ", self.fuel, " ", self.light, " ", self.seats)


class Bike(Vehicle):
    def __init__(self, engine, wheels, fuelTank, light, seats, handle):
        super().__init__(engine, wheels, fuelTank, light, seats)
        self.handle = handle

    def printBike(self):
        print(self.handle)


RE = Bike("v8", 2, 15, 1, 2, "bike handle")
RE.printVehicle()
RE.printBike().......................