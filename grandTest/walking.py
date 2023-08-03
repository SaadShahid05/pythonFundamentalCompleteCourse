
ask_distanceRange = 5
def distance(n):
    for i in range(1, n + 1):
        ask_distance = input("how long did you walk day " + str(i) + "? ")
distance(ask_distanceRange)