
import pygame as pg
from player import Player
from vector import Vector
from window import Window
from .translater import Translater


class PlayerTranslater(Translater):
    def translate(self, player: Player):
        keys = pg.key.get_pressed()
        vector = Vector(0, 0)
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

