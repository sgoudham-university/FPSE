from resources import playingCard


def determineWinner(hand):
    """Determines the winner of the game"""
    # Check if one player has a run
    # a run can be 4 cards in a row
    playingCard.sortHand(hand)


def main():
    deck = playingCard.generateDeck()
    deck = playingCard.shuffleCards(deck)
    hands = playingCard.dealCards(deck, 0, 5, [])
    print(hands)


main()
