#function should print, on the screen, the number of lines, words, and characters in the file


def characters(fileName):
    inFile = open(fileName, "r")
    content = inFile.read()
    print("the amount of characters inside of the file is: ", len(content))

characters("test.txt")

def words(fileName):
    inFile = open(fileName, "r")
    content = inFile.read()
    inFile.close()

    wordsList = content.split()
    print("these are the amount of words inside of the file: ", len(wordsList)) 

words("test.txt")

def lines(fileName):
    inFile = open(fileName, "r")
    lineAmount = inFile.readlines()
    print("the amount of lines inside of the file is: ", len(lineAmount))

lines("test.txt")

