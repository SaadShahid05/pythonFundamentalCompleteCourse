# factorial means that a number is multiplied by itself, and then a number less than it, 
# and then one less, and so on until it is muliplied by 1

number = int(input("enter your number here: "))

def findFact(value):
    fact = 1
    for i in range(1, value + 1):
        fact = fact * i # can also write: fact *= i
    return fact
print(findFact(number))

