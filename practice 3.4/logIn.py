logInId = input("enter a log in ID here: ")
logInList = ['joe', 'sue', 'hani', 'sophie']

if logInId in logInList:
    print("current user logger in: " + logInId)
    print("you are logged in")
    print("Done")
else:
    print("current user logger in: " + logInId)
    print("User unknown")
    print("Done")
