
monthsL = ["jan", "feb", "mar", "may"]
monthsT = ("jan", "feb", "mar", "may")

monthsL.insert(3, "apr")
# monthsT.insert(3, "apr") this will not work because it is a tuple

print(monthsL)
# print(monthsT)

monthsL.append("jun")
# monthsT.append("jun")

print(monthsL)
# print(monthsT)

#append

monthsL.append("jun")
print(monthsL)

#pop
monthsL.pop()
print(monthsL)

#remove second item:
monthsL.pop(1)
print(monthsL)

monthsL_reversed = monthsL.reverse()
#or you can do: 
monthsL_reversed2 = monthsL[::-1]
print(monthsL_reversed)
print(monthsL_reversed2)

#sort the container
monthsL.sort()
print(monthsL)

