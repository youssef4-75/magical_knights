import pygame as pg

from .player_interaction import PlayerInteraction
from utils import MAX_HP, MAX_MP, PLAYER, PLAYER_SIZE, SPEED

from .control_pannel import ControlPannel
from .game_object import GameObject



class Player(GameObject):
    """A class to represent a player in the game"""
    def __init__(self, name, color, init_pos, control_pannel: ControlPannel):
        super().__init__(*init_pos, *PLAYER_SIZE, color)
        self.__interaction_core = PlayerInteraction(MAX_HP, MAX_MP)
        self.name = name
        self.color = color
        self.speed = SPEED
        self.control = control_pannel

    def typeIdentifier(self):
        return PLAYER
        
    @property
    def interact(self):
        return self.__interaction_core
    
    def __repr__(self) -> str:
        return f"Player<{self.name}, color={self.color}, rect={self.rect}, alive={self.is_alive()}>"

    def draw(self, window):
        return window.draw(self.surf, self.rect)

    def translate(self):
        ...

    def is_alive(self):
        return self.interact.is_alive()