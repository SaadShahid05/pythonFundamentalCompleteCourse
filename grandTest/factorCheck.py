enterNumber = int(input("enter your number here: "))
def factor_chck(num):
    if num % 3 == 0 and num % 5 == 0:
        print("perfect")
    elif num % 3 == 0:
        print("trio")
    elif num % 5 == 0:
        print("Pent")
    elif num % 3 != 0 or num % 5 != 0:
        print("zip")

factor_chck(enterNumber)