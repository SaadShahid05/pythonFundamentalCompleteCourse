class movies:
    def __init__(self, name, release, score) -> None:
        self.name = name
        self.release = release
        self.score = score

    def showMovie(self):
        print(f"{self.name} - Release year: {self.release}, score: {self.score}")

# creating the objects:

movie1 = movies("Inception", 2010, 8.8)
movie2 = movies("The martian", 2015, 8.0)
movie3 = movies("Joker", 2019, 8.4)

# method:
movie1.showMovie()
print()
movie2.showMovie()
print()
movie3.showMovie()
print()
