


from services import ServicesManager
from utils import Vector
from utils.variables import REPULSE
from .registry import InteractionsRegistry
from objects import Player
from utils import PLAYER

@InteractionsRegistry.add_to_me(PLAYER, PLAYER)
def Player2Player(player1: Player, player2: Player):
    sm = ServicesManager.single()
    vector12 = Vector(*player1.rect.center) - Vector(*player2.rect.center)
    r = vector12.magnitude()
    if r==0:
        return 
    direction = (REPULSE/r) * vector12.normalize()
    print(direction)
    sm.repeller.repel(player1, -direction)
    sm.repeller.repel(player2, direction)
    