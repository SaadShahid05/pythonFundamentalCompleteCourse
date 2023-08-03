string = input("enter a string here to check wether it is a palindrome or not: ").casefold()
string2 = string[::-1] # reverses "string"

if string == string2:
    print("this is a palinrome")
else:
    print("this is not a palindrome")