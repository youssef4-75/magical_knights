import pygame as pg

from utils import Animation
from game import GameManager

from objects import Player

# from plugins import WithBackGround, WithPDisplayer
from utils import consolify, attach_grimoire, Vector, PLAYER_SIZE, from_root
from .actions import grimoire1, grimoire2


def main(game: GameManager, win_size):
    control1 = consolify(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
    control2 = consolify(pg.K_w, pg.K_s, pg.K_a, pg.K_d)
    control3 = consolify(pg.K_y, pg.K_h, pg.K_g, pg.K_j)
    control4 = consolify(pg.K_f, pg.K_v, pg.K_c, pg.K_b)

    animation = Animation.from_directory(from_root("assets/anim_set01/1x1"), PLAYER_SIZE)

    @game.add
    @attach_grimoire(grimoire2)
    def player(): 
        p = Player("riyad", "red", Vector.random(*win_size).to_tuple(), control1)
        p.attach_animation(animation)
        return p

    @game.add
    @attach_grimoire(grimoire1)
    def player(): 
        p = Player("mohssine", "blue", Vector.random(*win_size).to_tuple(), control2)
        p.add_actions(grimoire1)
        # p.add_action(pg.K_p, action=jump)
        return p

    @game.add
    def player(): return Player("othmane", "green", Vector.random(*win_size).to_tuple(), control3)

    @game.add
    def player(): return Player("yassine", "yellow", Vector.random(*win_size).to_tuple(), control4)

