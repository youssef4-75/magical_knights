
from utils.variables import REPULSE
from .registry import InteractionsRegistry
from objects import Player
from utils import PLAYER

@InteractionsRegistry.add_to_me(PLAYER, PLAYER)
def Player2Player(player1: Player, player2: Player):
    if not player1.is_alive() or not player2.is_alive():
        return
    
    