import pygame as pg

from ..mixins import ConsciousMixin
from ..game_object import GameObject

from utils import MAX_HP, MAX_MP, PLAYER_CLASS, PLAYER_SIZE, SPEED


class Player(GameObject, ConsciousMixin):
    """A class to represent a player in the game"""
    def __init__(self, name, color, init_pos, console: dict[str, int]):
        super().__init__(*init_pos, *PLAYER_SIZE, color, SPEED, HP=MAX_HP, MP=MAX_MP)
        ConsciousMixin.start(self, console)
        self.name = name

    def typeIdentifier(self):
        return PLAYER_CLASS
    
    def __repr__(self) -> str:
        return f"Player<{self.name}, rect={self.rect}, alive={self.is_alive()}>"


