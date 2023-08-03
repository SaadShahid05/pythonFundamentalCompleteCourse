import math 
heightInp = eval(input("enter the height here: "))
radiusInp = eval(input("enter a radius here: "))
formula = (2*math.pi*radiusInp*heightInp) + (2*math.pi*radiusInp**2)
def area(radius, height):
    return formula

print(f"the area of the cylinder is {area(radiusInp, heightInp)}") #formated it so it looks better
