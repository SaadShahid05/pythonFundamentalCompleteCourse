import random

chipAmount = 7

# deck = {"ace": 4, "card2": 4, "card3": 4, "card4": 4, "card5": 4, "card6": 4, "card7": 4, 
#         "card8": 4, "card9": 4, "card10": 4, "king": 4, "Queen": 4, "Jack": 4}
# deckValues = {"ace": [1,11], "card2": 2, "card3": 3, "card4": 4, "card5": 5, "card6": 6, "card7": 7, 
#         "card8": 8, "card9": 9, "card10": 10, "king": 10, "Queen": 10, "Jack": 10}

deck = {"card1": 4, "card2": 4, "card3": 4, "card4": 4, "card5": 4, "card6": 4, "card7": 4, 
        "card8": 4, "card9": 4, "card10": 4, "ace": 4, "king": 4, "Queen": 4, "Jack": 4}
deckValues = {"card1": 1, "card2": 2, "card3": 3, "card4": 4, "card5": 5, "card6": 6, "card7": 7, 
        "card8": 8, "card9": 9, "card10": 10, "ace": 11, "king": 10, "Queen": 10, "Jack": 10}

while True:         # it will loop as long as the content inside of the loop is true
    betAmount = int(input("How many do you bet?: "))
    if betAmount == 0:
        print("you cannot bet 0, bet again")
    elif betAmount >= chipAmount:
        print(f"you cannot bet more than the amount of chips you have. You have {chipAmount} chips in total")
    else: 
        print(f"you bet {betAmount} total")
        break

userCards = []
userCardsTotalValue = 0
dealerCards = []
dealerCardsTotalValue = 0

for i in range(2):
    randomCard = random.choice(list(deck.keys()))
    userCardsTotalValue += deckValues[randomCard]
    deck[randomCard] -= 1
    userCards.append(randomCard)

for i in range(2):
    randomCard = random.choice(list(deck.keys()))
    dealerCardsTotalValue += deckValues[randomCard]
    deck[randomCard] -= 1
    dealerCards.append(randomCard)

# for i in range(2):
#     randomCard = random.choice(list(deck.keys()))
#     if randomCard == "ace":
#         randomCardValue = random.choice(deckValues[randomCard])
#     else:
#         randomCardValue = deckValues[randomCard]
#     userCardsTotalValue += randomCardValue
#     deck[randomCard] -= 1
#     userCards.append(randomCard)

# # Draw two cards for the dealer
# for i in range(2):
#     randomCard = random.choice(list(deck.keys()))
#     if randomCard == "ace":
#         randomCardValue = random.choice(deckValues[randomCard])
#     else:
#         randomCardValue = deckValues[randomCard]
#     dealerCardsTotalValue += randomCardValue
#     deck[randomCard] -= 1
#     dealerCards.append(randomCard)

print(f"you have {userCards[0]} and {userCards[1]} with total value of: {userCardsTotalValue}")
print(f"The dealers visible card is a {dealerCards[0]}, with a value of {deckValues[dealerCards[0]]}. ")

#check if player has Ace and 10

def hitOrStand():
    global userCardsTotalValue
    print("Do you wish to hit or stand?\n1 - Hit\n2 - Stand")
    userInp = int(input("Enter 1 or 2: "))
    if userInp == 1 and userCardsTotalValue <= 21:
        print("You chose to hit")
        randomCard = random.choice(list(deck.keys()))
        userCardsTotalValue += deckValues[randomCard]
        deck[randomCard] -= 1
        userCards.append(randomCard)
        print(f"you have been dealt one card ({randomCard}). You Hand now consists of the of the following cards:")
        for card in userCards:
            print(card)
        print(f"The total value of your hand is now {userCardsTotalValue}, and the dealers is {deckValues[dealerCards[0]]}")
        if userCardsTotalValue > 21:
            return print(f"You have Busted. The dealer wins {betAmount} chips")
        else:
            hitOrStand()
    elif userInp == 2:
        print("You chose to stand")
        
    else:
        print("Invalid input. Please enter 1 or 2.")
        hitOrStand()

if userCardsTotalValue == 21:
    print(f"You have a combined value of 21 and thus you have won {betAmount * 2}!")
else:
    hitOrStand()

def dealerDrawCards():
    global dealerCardsTotalValue
    if dealerCardsTotalValue < 17:
        randomCard = random.choice(list(deck.keys()))
        dealerCardsTotalValue += deckValues[randomCard]
        deck[randomCard] -= 1
        dealerCards.append(randomCard)
    elif dealerCardsTotalValue > 21:
        print("The Dealer has Busted. Player Wins!")

dealerCardsTotalValue()
