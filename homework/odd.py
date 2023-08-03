#for loop
theRange = range(11,102)
for i in theRange: 
    if i % 2 != 0:
        print(i)
    else:
         print("X")


#While loop:
start = 11
while start < 102:
    if start % 2 != 0:
        print(start)
        start += 1
    else:
        print("X")
        start += 1