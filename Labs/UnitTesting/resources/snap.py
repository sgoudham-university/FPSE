import time

from resources import playingCard

userHand = 0
computerHand = 1


# Function: initialiseScore
# Description: Initialises who turn it is the computer of the user and how many winning hands
def initialiseScore():
    return [{"turn": True, "score": 0}, {"turn": False, "score": 0}]


# Function: isSnap
# Description: Determine if it is snap by comparing two playing cards
def isSnap(previousCard, nextCard):
    snap = False
    if previousCard[0] == nextCard[0]:
        snap = True
    return snap


# Function: playCard
# Description: Deals a card from either the computer or the users hands and prompts the console. The next card dealt
# from either hand is then returned.
def playCard(currentScore, hands):
    if currentScore[computerHand]["turn"]:
        nextCard = playingCard.dealACard(hands[1])
        prompt = "Computer plays "
        currentScore[computerHand]["turn"] = False
    else:
        # The next function returns a playing card. The playing card is the next card from the users hand. A list
        # "hands" is a list of lists of cards. The constant playCard.userHand is used to get the hand of cards for the
        # user
        nextCard = playingCard.dealACard(hands[playingCard.userHand])
        prompt = "You played "
        currentScore[userHand]["turn"] = False
    print(prompt + nextCard)
    return nextCard


# Method: determineWinner
# Description: Determine if the computer or the user has won and display the result. If the user call snap they must do
# it in a given time set by the user.
def determineWinner(currentScore, previousCard, nextCard, answer, waited, secondsToWait):
    if answer == "S" and isSnap(previousCard, nextCard) and waited < secondsToWait:
        print("Correct you win in " + str(waited))
        currentScore[userHand]["score"] += 1
        print("You have won " + str(currentScore[userHand]["score"]) + " hands")
    elif answer == "S" and isSnap(previousCard, nextCard) and waited > secondsToWait:
        print("Sorry to slow you waited " + str(waited))
        print("Computer wins")
        currentScore[computerHand]["score"] += 1
        print("Computer has won " + str(currentScore[computerHand]["score"]) + " hands")
    elif answer == "S" and not isSnap(previousCard, nextCard):
        print("Wrong the cards are different")
    elif answer == "N" and isSnap(previousCard, nextCard):
        print("Computer wins")
        currentScore[computerHand]["score"] += 1
        print("Computer has won " + str(currentScore[computerHand]["score"]) + " hands")


# Method: main
# Description: The main logic for snap given a hands of cards and a wait time.
def snap(hands, secondsToWait):
    answer = "N"
    nextCard = "  "
    currentScore = initialiseScore()
    while answer in ["N", "S"]:
        previousCard = nextCard
        nextCard = playCard(currentScore, hands)
        start = time.time()
        answer = input("Please enter (S)nap or (N)ext")
        waited = time.time() - start
        determineWinner(currentScore, previousCard, nextCard, answer, waited, secondsToWait)


def main():
    deck = playingCard.generateDeck()
    deck = playingCard.shuffleCards(deck)
    print("We will play snap to match on suites")
    secondsToWait = int(input("Please enter the number of seconds to wait"))
    # The next function returns two hands of cards. It has a full deck of cards as an input. The number of cards to deal
    # is zero so all cards are dealt to the two players. The last parameter is an empty list since the players have not
    # already been dealt any cards.
    hands = playingCard.dealCards(deck, 0, 2, [])
    snap(hands, secondsToWait)


main()
