b = int(input("enter your 'b' value here: "))
a = int(input("enter your 'a' value here: "))
c = int(input("enter your 'c' value here: "))

quadricFirst = (-1*b)
quadricSecond = ((b**2)-(4*a*c))**0.5
quadricWholePlus = (quadricFirst + quadricSecond) / 2*a
quadricWholeNegative = (quadricFirst - quadricSecond) / 2*a

print("x = " + str(quadricWholePlus))
print("x = " + str(quadricWholeNegative))

