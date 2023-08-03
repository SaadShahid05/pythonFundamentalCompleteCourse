name = input("enter your name here: ")

choice = input("for lowercase write 'lower', for uppercase write 'upper' and for titlecase write 'title'. Write here: ")

if choice == "lower":
    print(name.lower())
elif choice == "upper":
    print(name.upper())
elif choice == "title":
    print(name.title())
else:
    print("not a valid input")
