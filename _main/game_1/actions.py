import pygame as pg

from game import GameManager
from objects import Player, Energy, Material
from utils import Vector, actionify_deco, ENERGY_SIZE 

grimoire1 = {}
grimoire2 = {}

@actionify_deco(grimoire1, pg.K_o, mana=10, cooldown=120, initial_delay=10)
def jump(player: Player, *a, **k):
    player.set_accel(10*Vector.up())


@actionify_deco(grimoire1, pg.K_p, mana=0, cooldown=120, initial_delay=10)
def energy_shooter(player: Player, game: GameManager):
    e = Energy(
        player.spell_pos(up=ENERGY_SIZE//2 + 30 ),
        # (player.rect.centerx, player.rect.top - ENERGY_SIZE - 10),
        2,
        Vector.up(),
        TTL=200
    )
    game.append(e)

@actionify_deco(grimoire2, pg.K_i, mana=10, cooldown=100, initial_delay=0)
def material(player: Player, game: GameManager):
    m = Material("grey", player.spell_pos(left=30), (10, 30))
    game.append(m)