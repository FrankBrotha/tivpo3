import random
class Card:
    SUITS = ['♠', '♣', '♦', '♥']
    RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return f'{self.rank}{self.suit}'
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        random.shuffle(self.cards)
    def draw(self):
        return self.cards.pop() if self.cards else None
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def draw_cards(self, deck, count=6):
        for _ in range(count):
            card = deck.draw()
            if card:
                self.hand.append(card)
    def attack(self):
        return self.hand.pop(0) if self.hand else None
    def defend(self, attack_card, trump_suit):
        for card in self.hand:
            if (card.suit == attack_card.suit and Card.RANKS.index(card.rank) > Card.RANKS.index(attack_card.rank)):
                self.hand.remove(card)
                return card
        for card in self.hand:
            if card.suit == trump_suit:
                self.hand.remove(card)
                return card
        return None
class DurakGame:
    def __init__(self, player1, player2):
        self.deck = Deck()
        self.players = [Player(player1), Player(player2)]
        self.trump = self.deck.draw()
        self.attacker = self.players[0]
        self.defender = self.players[1]

    def turn(self):
        attack_card = self.attacker.attack()
        if not attack_card:
            return f'{self.defender.name} победил!'
        defense_card = self.defender.defend(attack_card, trump_suit=self.trump.suit)
        if defense_card:
            result = f'{self.defender.name} отбился {defense_card} против {attack_card}'
            self.attacker, self.defender = self.defender, self.attacker
            return result
        else:
            self.defender.draw_cards(self.deck, 1)
            return f'{self.attacker.name} победил!'
    def is_game_over(self):
        return not self.attacker.hand or not self.defender.hand
