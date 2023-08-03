#if a word has 6 letters or more, it is considedred to be a big word

wordInp = input("enter your word here: ").split()
def findBigWord(n):
    for word in n:
        if len(word) >= 6:
            print("'" + word + "'", " is a big word")
        else:
            print()
findBigWord(wordInp)