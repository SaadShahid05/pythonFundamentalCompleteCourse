
def distribution(filename):
    file = open(filename, "r")
    readfile = file.read()
    readfileList = readfile.split()
    randomList = []
    for score in readfileList:
        if score in randomList:
            print()
        else: 
            randomList.append(score)
            counter = readfileList.count(score)
            print(counter, "students got", score)
    
distribution("dis.txt")

