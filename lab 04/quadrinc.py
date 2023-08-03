import math

a = int(input("enter your 'a' value here: "))
b = int(input("enter your 'b' value here: "))
c = int(input("enter your 'c' value here: "))
squareRoot = ((b**2-(4*a*c)))**0.5

if a * 2 == 0:
    print("the equation cannot solve as there is a zero division")
else: 
    firstSolution = (-b + squareRoot) / (2*a)
    secondSolution = (-b - squareRoot) / (2*a)
    print("first x value is: " + str(firstSolution))
    print("the second x value is: " + str(secondSolution))
    
