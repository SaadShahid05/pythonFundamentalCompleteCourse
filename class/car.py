class car():
    def __init__(self, plateNumber, xLocation, yLocation, speed) -> None:
        self.plateNumber = plateNumber
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.speed = speed

    def plate(self):
        self.plateNumber

    def x(self):
        self.xLocation
    
    def y(self):
        self.yLocation

    def speeds(self):
        self.speed

car1 = car("NO-A8971", 55.12, 2151.1221, "55kmh")
car2 = car("SE-B8317", 1215.1512, 125.21, "99kmh")
car3 = car("DE-C1071", 1501, 11, "0kmh")

print(car1.speeds())
print(car2.speeds())
print(car3.speeds())

        