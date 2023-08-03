class soccerPlayer():
    def __init__(self, name, number, xlocation, yLocation) -> None:
        self.n = name
        self.num = number
        self.xL = xlocation
        self.yL = yLocation

    def run(self):
        print(f"{self.name} is running at x-coordinate: {self.xLocation} and y-coordinate: {self.yLocation}")

    def jump(self):
        print(f"{self.name} with the number {self.number} jumped at x location: {self.xLocation} and y location: {self.yLocation}")

    def kickBall(self):
        print(f"{self.name} with the number {self.number} kicked the ball at x location: {self.xLocation} and y location: {self.yLocation}")


player1 = soccerPlayer("Ronaldo", 7, 22.125, 82.2151)
player2 = soccerPlayer("Messi", 11, 66, 9.1209)
player3 = soccerPlayer("Neymar", 10, 97.1251, 12)

print(player1.run())
print(player2.run())
print(player2.run())

print(player1.kickBall())
print(player2.kickBall())
print(player2.kickBall())


        