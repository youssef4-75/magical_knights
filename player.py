import pygame as pg

from control_pannel import ControlPannel
from game_object import GameObject
from vector import Vector


class Player(GameObject):
    """A class to represent a player in the game"""
    def __init__(self, name, color, control_pannel: ControlPannel):
        super().__init__(300, 300, 30, 30, color)
        self.name = name
        self.color = color
        self.HP = 100
        self.MP = 100
        self.speed = 100
        self.control = control_pannel
        

    def __str__(self) -> str:
        return f"Player<{self.name}, color={self.color}>"