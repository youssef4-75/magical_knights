import pygame as pg

from utils import MAX_HP, MAX_MP, PLAYER, PLAYER_SIZE, SPEED

from .control_pannel import ControlPannel
from .game_object import GameObject



class Player(GameObject):
    """A class to represent a player in the game"""
    def __init__(self, name, color, init_pos, control_pannel: ControlPannel):
        super().__init__(*init_pos, *PLAYER_SIZE, color, SPEED, HP=MAX_HP, MP=MAX_MP)

        self.name = name
        self.control = control_pannel

    def typeIdentifier(self):
        return PLAYER
    
    def __repr__(self) -> str:
        return f"Player<{self.name}, color={self.color}, rect={self.rect}, alive={self.is_alive()}>"

    def draw(self, window):
        return window.draw(self.surf, self.rect)

    def translate(self):
        ...
