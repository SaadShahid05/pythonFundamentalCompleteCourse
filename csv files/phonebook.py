# import csv
# file = open("p.csv", "a")

# name = input("enter a name: ")
# number = int(input("enter a number here: "))

# writer = csv.writer(file)
# writer.writerow([name,number])
# file.close()

# Saves names and numbers to a CSV file

import csv

# Open CSV file
file = open("p.csv", "a")

# Get name and number
name = input("Name: ")
number = input("Number: ")

# Print to file
writer = csv.writer(file)
writer.writerow([name, number])

# Close file
file.close()