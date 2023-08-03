books = ["The Hobbit", "Farmer Giles of Ham", "The fellowship of the ring", "The two towers", 
         "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf",]
print(books[0], ", ", books[1], ", ", books[-1], ", ", books[-2])

books.append("The Silmarillion")
books.append("Unfinished Tales")
print(books)

for book in books:
    if book == "The fellowship of the ring" or book == "The two towers" or book == "The Return of the King":
        books[books.index(book)] = f"Lord Of The Rings {book}"

# for book in books:
#     if book == "The fellowship of the ring" or book == "The two towers" or book == "The Return of the King":
#         book = f"Lord of the rings {book}"    

# books[books.index("The fellowship of the ring")] = "Lord Of The rings The fellowship of the ring"

# print(books.sort())

print(books)