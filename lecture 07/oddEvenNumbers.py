listOfOddNumbers = []
listOfEvenNumbers = []
def findOddNumbers(list):
    for number in list:
        if number % 2 == 0:
            listOfEvenNumbers.append(number)
            print(str(number) + " is an even number")
        else:
            listOfOddNumbers.append(number)
            print(str(number) + " is an odd number")

print(findOddNumbers([2,5,1,4,7,23,24,12,88,67]))
print("here is the list of all the odd numbers: " + str(listOfOddNumbers))
print("here is the list of all the even numbers: " + str(listOfEvenNumbers))
