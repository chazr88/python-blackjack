import random
import itertools


#Itertools is used to multiply the 1st element of the first array with every element of the 2nd array. 
#EX ('A', 'Spade'), ('A', 'Club'), ('A', 'Diamond'), ('A', 'Heart')
cardDeck = list(itertools.product(["A","2","3","4","5","6","7","8","9","10","J","Q","K"],["Spade", "Club", "Diamond", "Heart"]))

playing = True;

dealerHand = []
playerHand = []


def shuffle():
    random.shuffle(cardDeck)

def dealCard(person):
    card = cardDeck[0]
    cardDeck.remove(card)
    if card[0] == 'A':
        if person == playerHand:
            chooseAce(card)
        else:
            dealerChooseAce(card)
    else:
        person.append(card)

def removeCard(card):
    cardDeck.remove(card)

def dealerChooseAce(card):
    if addUpCards(dealerHand) <= 10:
        card = card + (11,)
        dealerHand.append(card)
    else: 
        card = card + (1,)
        dealerHand.append(card)

def chooseAce(card):
    print(playerHand)
    choice = input("Would you like your Ace to be 1 or 11?")
    if choice == "1":
        print(card)
        card = card + ('1',)
        print(card)
        playerHand.append(card)
    elif choice == "11":
        card = card + ('11',)
        playerHand.append(card)
    else:
        print("Sorry you must choose 1 or 11.")
        chooseAce()


#Adds up all the cards in the hand
def addUpCards(hand):
    sum = 0
    for count,card in enumerate(hand):
        if card[0] == 'K' or card[0] == 'Q' or card[0] == 'J':
            sum += 10
        elif card[0] == 'A':
            sum += int(card[2])
        else:
            sum += int(card[0])
    return(sum)

#Adds up all the cards in the hand except the first one. This is so the dealer wont know the face down card. 
def faceUpAdd(hand):
    sum = 0
    for count,card in enumerate(hand[1:]):
        if card[0] == 'K' or card[0] == 'Q' or card[0] == 'J' or card[0] == 'A':
            sum += 10
        else:
            sum += int(card[0])
    return(sum)

def initialDeal():
    shuffle()
    dealCard(playerHand)
    dealCard(dealerHand)
    dealCard(playerHand)
    dealCard(dealerHand)

#Player must choose to hit or pass
def choice():
    print(f"Your Hand, {playerHand}")
    print(f"The Dealer's Hand, {dealerHand[1:]}")
    print("1 Hit")
    print("2 Pass")
    return input("What would you like to do?")

def dealerTurn():
    dealerCards = addUpCards(dealerHand)
    playerCards = faceUpAdd(playerHand)
    if dealerCards < 17 or dealerCards < playerCards:
        dealCard(dealerHand)
        calculate(dealerHand)
        dealerTurn()
    else:
        return

def calculate(hand):
    if(addUpCards(hand) > 21): 
        if hand == playerHand:
            print(playerHand)
            print("Player Busted")
            print("Sorry You Loose")
            exit()
        else:
            print("Dealer Busted")
            print("You Win!")
            exit()
        return False
    else:
        return True

def choose():
    myChoice = choice()
    if myChoice == '1':
        dealCard(playerHand)
        calculate(playerHand)
        choose()
    else:
        dealerTurn()


while playing:
    print("####################################")
    print("             BLACK JACK             ")
    print("####################################")
    initialDeal()
    choose()
    print(playerHand)
    print(dealerHand)
    if addUpCards(playerHand) > addUpCards(dealerHand):
        print("Player Had The Better Hand")
        print("You Win!")
    elif addUpCards(playerHand) == addUpCards(dealerHand):
        print("Its A Tie!")
    else:
        print("Dealer Had The Better Hand")
        print("Sorry You Loose")
    playing = False
