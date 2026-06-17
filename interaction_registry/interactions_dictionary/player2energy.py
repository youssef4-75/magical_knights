


from .tools import reclassify, register
from ...utils import ENERGY_CLASS, PLAYER_CLASS
from ...objects import Energy, Player

@register(PLAYER_CLASS, ENERGY_CLASS)
def Player2Energy(_player: Player, _energy: Energy):
    player, energy = reclassify(_player, _energy, _1st_class=Player, _2nd_class=Energy)
    player.damage(energy.MP)
    energy.consume(energy.MP)