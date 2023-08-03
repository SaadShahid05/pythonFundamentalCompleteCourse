# make 4 functions crud (creat, read, update, delete) operations

# def createFile(data, type, fileName):
#     with open(f"{fileName}.{type}", "a") as file:
#         file.write(data)
# createFile("my name is Sa'd", "js", "intro")


# def readFile(fileName):
#     read = []
#     with open(fileName, "r") as file:
#         for line in file:
#             read.append(line.strip())
#     return read
# # print(readFile("intro.txt"))


# def updateFile(fileName, newData):
#     read = readFile(fileName)   
#     with open(fileName, "w") as file: 
#         file.write(newData) 
# updateFile("intro.txt", "yeh bate achi nahi he")


# def deleteRecord(fileName):
#     read = readFile(fileName)   
#     with open(fileName, "w") as file: 
#         file.write("\n")
# deleteRecord("intro.txt") 

import os

def deleteFile(fileName):
    try:
        os.remove(fileName)
        print("file has been deleted")
    except OSError as e:
        print(f"could not be deleted because it is not found {e}")
deleteFile("intro.doc")
