import math

class Circle:
    def __init__(self, radius, color) -> None:
        self.radius = radius    #instance variables (data of class, also called attributes)
        self.color = color

    #methods/functions/object behaviour: 

    def getRadius(self):
        return self.radius

    def getArea(self):
        return math.pi*self.radius**2 

    def getCircumfarenceOfCircle(self):
        return 2*math.pi*self.radius

#creating objects

circle1 = Circle(12,"red")
circle2 = Circle(1,"greed")
circle3 = Circle(55,"blue")

print(circle1.getRadius())
print(circle2.getRadius())
print(circle3.getRadius())

print(circle1.color)
print(circle2.color)
print(circle3.color)

print(f"the area of circle 1: {circle1.getArea()}")
print(f"the area of circle 2: {circle2.getArea()}")
print(f"the area of circle 3: {circle3.getArea()}")

print(circle1.getRadius())
print(circle2.getRadius())
print(circle3.getRadius())

