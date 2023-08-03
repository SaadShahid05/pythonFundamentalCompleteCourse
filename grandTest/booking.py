name = input("enter your name here: ")
surname = input("enter your surname here: ")
destination = input("enter your destination here: ").title()
acceptedDesitnations = ["Oslo", "Paris", "Singapore", "New york"]

def bookings():
    booking = {"name": name, "surname": surname, "destination": destination}
    for item in booking.values():
        if len(item) == 0 or item == " ":
            print("you need to fill all the fields")
        else:
            print("success")
    
    if booking["destination"] in acceptedDesitnations:
        print("your destination is:", booking["destination"])
    else:
        print("This destiantion is not accepted, please enter another desitation")

print(bookings())

