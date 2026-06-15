import pygame as pg

from objects.conscious_mixin import ConsciousMixin
from utils import MAX_HP, MAX_MP, PLAYER, PLAYER_SIZE, SPEED

from .game_object import GameObject



class Player(GameObject, ConsciousMixin):
    """A class to represent a player in the game"""
    def __init__(self, name, color, init_pos, console: dict[str, int]):
        super().__init__(*init_pos, *PLAYER_SIZE, color, SPEED, HP=MAX_HP, MP=MAX_MP)
        ConsciousMixin.start(self, console)
        self.name = name

    def typeIdentifier(self):
        return PLAYER
    
    def __repr__(self) -> str:
        return f"Player<{self.name}, rect={self.rect}, alive={self.is_alive()}>"

    def draw(self, window):
        return window.draw(self.surf, self.rect)

    def translate(self):
        ...
