import csv

moviesList = ["The Lion King - 1994 has a rating of 8.5", "Inception - 2010 has a rating of 8.8", 
              "The Shawshank Redemption - 1994 has a rating of 9.3", "Pulp Fiction - 1994 has a rating of 8.9", 
              "The Dark Knight - 2008 has a rating of 9.2", "Schindler's List - 1993 has a rating of 8.9"]

def movies(filename):
    with open((filename), "a") as moveiFile:
        for movie in moviesList:
            moveiFile.write(f"({movie}) \n")
# movies("movies.txt")

def readMovies(filename):
    with open(filename, "r") as movieFile:
        readFile = csv.DictReader(movieFile)
        i = 1
        for line in readFile:
            print(f"{i}: {line['movie']}")
            i += 1
readMovies("movies.txt")
