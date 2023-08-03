message = "this is a top secret message and shuold not be divulged to anyone without top secret clearance"
s = ("top secret")
print("user has given the message: ", message)
print("the string that is needed to find is: ", s)
print("string find method () :", message.find(s))
print("the string to be found has occured: ", message.count(s), "times")
print("the message has now been changed using replace(): ", message.replace("top", "no"))