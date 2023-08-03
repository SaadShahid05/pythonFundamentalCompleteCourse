
# def stats(name):
#     file = open(name, "r")
#     content = file.read()

#     characters = len(content)

#     words = len(content.split())

#     lines = len(file.readlines())

#     print(f"The amount of characters inside of the file called: {name} is {characters} \n The amount of words inside of the file is {words} \n The amount of lines inside of the file is {lines}" )

# stats("test.txt")


# f = open("class.txt", "w")

with open("class.txt", "a") as file:
    file.write("My name is Saad Shahid \n")
    file.write("i am 18 years old \n")
    file.write("my teacher is Zakariya \n")
    file.write("hello world \n")
    