phraseInp = input("enter your phrase here: ").split()

def phrase(phrase):
    if len(phrase) >= 3:
        print(phrase[0:3], end=" , ")
    elif len(phrase) < 3:
        print(phrase)
    
        
phrase(phraseInp)


def middle(phrase):
    if len(phrase) % 2 == 0:
        middlePhrases = len(phrase) // 2
        print(phrase[middlePhrases-1 : middlePhrases+1])
    elif len(phrase) % 2 != 0:
        middlePhrases = len(phrase) // 2
        print(phrase[middlePhrases-1 : middlePhrases+2])

middle(phraseInp)


def lastWords(phrase):
    if len(phrase) >= 3:
        print(phrase[-3:-1])
    else:
        print(phrase)

lastWords(phraseInp)

