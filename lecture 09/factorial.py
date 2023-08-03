findFactor = int(input("enter a number here: "))

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(findFactor))


lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, 99]
result = []
for i in lst:
    result.append(factorial(i))
print(result)