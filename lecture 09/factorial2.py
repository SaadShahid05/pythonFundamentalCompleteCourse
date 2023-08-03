factorialNum = int(input("enter your number here: "))

def findFactorial(number):
    fact = 1 
    for i in range(1, number + 1):
        fact *= i
    print(fact)
findFactorial(factorialNum)
