def openfile():
    file = open("test.txt", "r")
    content = file.read()
    print(content)
openfile()

def readfile():
    file = []
    with open ("test.txt", "r") as something:
        for everyLine in something:
            file.append(everyLine)
    return file
print(readfile())

# def howmanylines():
#     file = open("test.txt", "r")
#     lines = file.readline()
#     print(lines)
# howmanylines()

