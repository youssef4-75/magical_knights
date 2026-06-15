from utils.variables import PLAYER_CLASS
from .tools import reorder

from .player2player import Player2Player


registry = {
    reorder(PLAYER_CLASS, PLAYER_CLASS): Player2Player
}

# add_to_registry(registry, PLAYER, PLAYER, Player2Player)
