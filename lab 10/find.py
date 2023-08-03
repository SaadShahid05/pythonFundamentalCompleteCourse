check = input("enter a key and check if it is inside of the dictionary: ")
dict = {"name": "Ibrahim", "Age": 12, "Class": "Tenth", "DOB": "16 April 2005"}

if check in dict:
    print("yes, ", check, " is one of the keys in the dict dictionary")
else:
    print("no it is not inside of the dictionary")