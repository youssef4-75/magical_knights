


from .registry import InteractionsRegistry
from objects import Player
from utils import PLAYER

@InteractionsRegistry.add_to_me(PLAYER, PLAYER)
def Player2Player(player1: Player, player2: Player):
    print(f"we are interacting here!!!, {player1} and {player2}")