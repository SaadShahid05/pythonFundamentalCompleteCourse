age = int(input("enter a random age here: "))

if age > 62:
    print("you can get your personal benefits")
else: 
    print("you dont get personal benefits")


name = ["Musial", "Aaraon", "Williams", "Gehrig", "Ruth"]
enterName = input("enter a name here: ")

for names in name:
    if names == enterName:
        print("One of the top baseball players")
    else: 
        print("not one of the top baseball players")

    

shield = int(input("how many shields are left: "))
hits = int(input("how many hits: "))

if hits > 10 & shield == 0:
    print("you are dead")
else:
    print("you are not dead")


north = True
south = False
west = False
east = False

if north == True or south == True or west == True or east == True:
    print("You can escape")
else:
    print("you are not able to escape")