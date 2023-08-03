
# def openFile():
#     with open("something.py", "a") as file:
#         file.write("this is just a little test")
# openFile()


# def numWord():
#     inFile = open("test.txt", "r")
#     content = inFile.read()
#     inFile.close()

#     wordList = content.split()
#     print(wordList)
#     return len(wordList)
# numWord()

# def lineList():
#     infile = open("test.txt", "r")
#     lineList = infile.readlines()
#     infile.close()

#     print(lineList)
# lineList()

# infile = open("test.txt")
# for line in infile:
#     print(line, end="")

# infile = open("test.txt")
# for line in infile:
#     if "test" in line:
#         print(line)
#     else:
#         print()

def addContent():
    outFile = open("text.txt", "a")
    addStuff = outFile.write('still the first line... \n')
    return addStuff
addContent()