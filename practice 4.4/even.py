evenNumber = int(input("enter your number here: "))
def even(n):
    for i in range(2, n):
        if i % 2 == 0 or i % 3 == 0:
            print(i)
        else: 
            print("x")

even(evenNumber)