year = int(input("enter a year here to check wether it is a leap year or not: "))

if year % 4 == 0:
    print("can be a leap year")
else: 
    print("can not be a leap year")

ticket = input("enter a ticket value: ") 
lotteryList = ["winner", "ticketMaster", "chance"]

if ticket in lotteryList:
    print("you have won")
else: 
    print("you have not won")