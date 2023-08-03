
def duplicate(filename):
    file = open(filename, "r")
    content = file.read().split()
    for i in content:
        if content.count(i) > 1:
            return print("there are some duplicates in this list")
        else:
            return print("False")

duplicate("dis.txt")

