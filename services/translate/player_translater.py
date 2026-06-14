
import pygame as pg
from objects import Player
from utils import Vector
from .translater import Translater


class PlayerTranslater(Translater):
    def translate(self, player: Player):
        keys = pg.key.get_pressed()
        vector = Vector()
        if keys[player.control.directions["up"]]:
            vector += Vector.up()
        if keys[player.control.directions["down"]]:
            vector += Vector.down()
        if keys[player.control.directions["left"]]:
            vector += Vector.left()
        if keys[player.control.directions["right"]]:
            vector += Vector.right()

        # if vector.magnitude()!= 0.0: print(vector)
        player.move(vector)

