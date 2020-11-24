import unittest

from resources import playingCard


class snapTest(unittest.TestCase):
    deck = playingCard.generateDeck()

    def dealACard(self):
        """Imitate dealing a card"""

        hand_length_before = len(self.deck)
        removed_card = playingCard.dealACard(self.deck)
        hand_length_after = len(self.deck)

        return hand_length_before, removed_card, hand_length_after

    def test_happy_generate_deck(self):
        """Test Deck"""

        self.assertTrue(52, len(self.deck))

    def test_unhappy_generate_deck(self):
        """Test Deck"""

        self.assertFalse(0, len(self.deck))

    def test_shuffle_cards(self):
        """Test shuffling cards"""

        unshuffled_deck = playingCard.generateDeck()
        shuffled_deck = playingCard.shuffleCards(self.deck)

        self.assertNotEqual(shuffled_deck, unshuffled_deck)

    def test_deal_a_card_length_decreased(self):
        """Test dealing a card - check if the length of the deck has decreased by 1"""

        hand_length_before, removed_card, hand_length_after = self.dealACard()

        self.assertTrue(hand_length_after == hand_length_before - 1)

    def test_deal_a_card_is_removed(self):
        """Test dealing a card - check if card exists within deck"""

        hand_length_before, removed_card, hand_length_after = self.dealACard()

        self.assertTrue(removed_card not in self.deck)

    def test_deal_cards_with_empty_hand(self):
        """Test dealing cards with empty hand"""

        generated_deck = playingCard.generateDeck()
        list_of_hands = playingCard.dealCards(generated_deck, 4, 13)

        self.assertTrue(len(generated_deck) == 0)

        for hand in list_of_hands:
            self.assertTrue(len(hand) == 4)

    def test_deal_cards_with_hand(self):
        """Test dealing with set hand"""

        hands = [["A3"], ["A4"], ["A5"], ["A7"]]

        generated_deck = playingCard.generateDeck()
        list_of_hands = playingCard.dealCards(generated_deck, 4, 13, hands)

        self.assertTrue(list_of_hands[0][0] == "A3")
