from .tools import add_to_registry, register

from .player2energy import Player2Energy
from .player2player import Player2Player
from .energy2energy import Energy2Energy
from .energy2material import Energy2Material

__list__ = [
    Player2Player,
    Player2Energy,
    Energy2Energy,
    Energy2Material,
]

registry = {}


for item in __list__:
    add_to_registry(registry, item)
# add_to_registry(registry, PLAYER, PLAYER, Player2Player)
