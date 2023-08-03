tekst = input("hello enter something: ")
def big(l):
    result = []
    for word in l:
        if len(word) >= 6:
            result.append(word)
            return word
        else:
            print() 
    print(result)
big(tekst)

