from utils import ENERGY_CLASS, PLAYER_CLASS

from .tools import add_to_registry

from .player2energy import Player2Energy
from .player2player import Player2Player

__list__ = [
    Player2Player,
    Player2Energy
]

registry = {}


for item in __list__:
    add_to_registry(registry, item)
# add_to_registry(registry, PLAYER, PLAYER, Player2Player)
