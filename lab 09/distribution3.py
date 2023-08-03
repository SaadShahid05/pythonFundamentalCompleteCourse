
def grades():
    file = open("dis.txt", "r") 
    content = file.read()
    contentList = content.split()
    print(contentList)

    for letter in contentList:
        counter = contentList.count(letter)
        print(f"{letter} has occured {counter} times")
        while letter in contentList:
            contentList.remove(letter)
grades()