from unittest import TestCase

from resources import playingCard


def setup():
    deck = playingCard.generateDeck()
    deck = playingCard.shuffleCards(deck)
    return playingCard.dealCards(deck, 0, 5, [])


class Test(TestCase):

    def test_playing_a_card(self):
        """Play a card"""
        hands = setup()
        player1 = hands[0]
        card_to_remove = player1[0]

        length_before_card_is_played = len(player1)
        playingCard.playACard(player1, card_to_remove)
        length_after_card_is_played = len(player1)

        self.assertEquals(length_after_card_is_played, length_before_card_is_played - 1)

    def test_determine_winner(self):
        """Determine the winner"""

        hands = setup()
