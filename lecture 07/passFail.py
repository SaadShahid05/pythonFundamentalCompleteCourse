
def exam():
    name = input("enter your name here: ")
    score = int(input("what was your exam score from 1 to 100: "))
    if score < 60:
        print(name + ", you did not pass the exam")
    elif score > 100:
        print("sorry " + name + ", this score is not possible to get, it is only possible to get a score from 1-100")
    elif score >= 60: 
        print(name + ", Congrats! You passed the exam!")
    

exam()