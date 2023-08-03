#function should print, on the screen, the number of lines, words, and characters in the file


def stats(fileName):
    inFile = open(fileName, "r")
    content = inFile.read()
    lineAmount = inFile.readlines()
    lineCount = len(lineAmount)
    print("amount of lines: ", lineCount)

    print("the amount of words inside of the text that is here is: ", len(content))
stats("test.txt")
