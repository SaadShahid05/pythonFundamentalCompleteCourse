names = input("enter a list of names with space in between them :").split() #making the input into a list 
print(names)
print("Four-letter words in the list:")
counter = 0
for word in names:  #printing the words that contain only 4 letters
    if len(word) == 4:
        counter += 1
        print(word)
        print("this many 4 letter words have occured: ", counter)