from behave import given, when, then
from game import DurakGame, Deck

@given('создана игра между "{player1}" и "{player2}"')
def step_create_game(context, player1, player2):
    context.game = DurakGame(player1, player2)

@given('Игроки получили начальные карты')
def step_players_draw(context):
    for player in context.game.players:
        player.draw_cards(context.game.deck)

@when('игроки получают карты')
def step_players_draw(context):
    for player in context.game.players:
        player.draw_cards(context.game.deck)

@then('у каждого игрока должно быть по 6 карт')
def step_check_cards(context):
    for player in context.game.players:
        assert len(player.hand) == 6

@when('"{attacker}" атакует "{defender}"')
def step_attack(context, attacker, defender):
    context.result = context.game.turn()

@then('"{defender}" должен попытаться защититься')
def step_defense(context, defender):
    assert "отбился" in context.result

@when('карты игроков заканчиваются')
def step_empty_hands(context):
    while not context.game.is_game_over():
        context.game.turn()

@then('игра должна завершиться')
def step_game_over(context):
    assert context.game.is_game_over()

@then('следующий ход должен сделать "{player}"')
def step_next_turn(context, player):
    assert context.game.attacker.name == player

@then('"{player}" должен атаковать "{opponent}"')
def step_player_attack(context, player, opponent):
    assert context.game.attacker.name == player
    context.result = context.game.turn()

@given('колода пуста')
def step_empty_deck(context):
    context.game.deck.cards = []

@when('"{player}" пытается взять карту')
def step_player_draw(context, player):
    player_obj = next(p for p in context.game.players if p.name == player)
    initial_hand_size = len(player_obj.hand)
    player_obj.draw_cards(context.game.deck)
    context.card_taken = len(player_obj.hand) > initial_hand_size;
    assert len(player_obj.hand) == initial_hand_size

@then('она не должна получать карту')
def step_no_card_received(context):
    assert not context.card_taken, "Игрок должен был получить карту, но этого не произошло"


