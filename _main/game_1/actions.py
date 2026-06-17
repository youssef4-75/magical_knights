import pygame as pg

from game import GameManager
from objects import Player, Energy
from utils import Vector, actionify_deco, ENERGY_SIZE 

grimoire1 = {}

@actionify_deco(grimoire1, pg.K_o, mana=10, cooldown=120, initial_delay=10)
def jump(player: Player, *a, **k):
    player.set_accel(10*Vector.up())


# @actionify_deco(grimoire1, pg.K_p, mana=20, cooldown=120, initial_delay=10)
# def energy_shooter(player: Player, game: GameManager):
#     ...
#     e = Energy(
#         (player.rect.centerx, player.rect.top - ENERGY_SIZE - 10),
#         20,
#         Vector.up()
#     )
#     game.append(e)

