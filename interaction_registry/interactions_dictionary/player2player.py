
from .tools import register
from ...objects import Player
from ...utils import PLAYER_CLASS, TOUCH_DAMAGE


@register(PLAYER_CLASS, PLAYER_CLASS)
def Player2Player(player1: Player, player2: Player):
    player1.damage(TOUCH_DAMAGE)
    player2.damage(TOUCH_DAMAGE)
    