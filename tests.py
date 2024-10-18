import unittest
from game import Card, Deck, Player, DurakGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.game = DurakGame("Alice", "Bob")
        self.player1 = self.game.players[0]
        self.player2 = self.game.players[1]

    def test_deck_size(self):
        self.assertEqual(len(self.deck.cards), 36)

    def test_player_draw_cards(self):
        self.player1.draw_cards(self.deck)
        self.assertEqual(len(self.player1.hand), 6)

    def test_attack_defense(self):
        self.player1.draw_cards(self.deck)
        card = self.player1.attack()
        self.assertIsNotNone(card)

    def test_defense_with_trump(self):
        self.player1.hand = [Card('6', '♠')]
        self.player2.hand = [Card('7', '♥')]
        trump_suit = '♥'
        attack_card = self.player1.attack()
        defense_card = self.player2.defend(attack_card, trump_suit)

        self.assertEqual(defense_card.suit, trump_suit)

    def test_game_over(self):
        while not self.game.is_game_over():
            self.game.turn()
        self.assertTrue(self.game.is_game_over())

    def test_trump_card(self):
        self.assertIsNotNone(self.game.trump)

if __name__ == '__main__':
    unittest.main()
