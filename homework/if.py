
usrInp =  input("What is the meaning of life? Hint: It is a number. ")
usrInp = int(usrInp)

if usrInp == 42:
    print("That's right, the meaning of life is 42!")
elif usrInp > 30 and usrInp < 50:
    print("close but not right")
else: 
    print("ERROR")