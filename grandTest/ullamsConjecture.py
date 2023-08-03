
# numberInp = int(input("enter your number here: "))

# def ullam(n):
#     if n != 1:
#         while n != 1:
#             if n % 2 == 0:
#                 n = n / 2
#                 print(n)
#             else:
#                 n = (n * 3) + 1
#                 print(n)
#     else:
#         print("input is equal to 1")

# ullam(numberInp)




enterNumber = int(input("enter a number here: "))
def ullam(n):
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = (n*3) + 1
            print(n)
    else:
        print("the number is 1")
ullam(enterNumber)
