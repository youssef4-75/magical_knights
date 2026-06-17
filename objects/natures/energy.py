
import pygame as pg

from utils import Vector

from utils import MAX_HP, MAX_MP, PLAYER_CLASS, ENERGY_SIZE, ENERGY_SPEED, ENERGY_CLASS

from ..game_object import GameObject

class Energy(GameObject):
    def __init__(self, init_pos, speed, direction: Vector, TTL: int = 200):
        super().__init__(*init_pos, ENERGY_SIZE, 
                ENERGY_SIZE, speed=speed,
                TTL=TTL, HP=10, vel=direction)
        

    def typeIdentifier(self):
        return ENERGY_CLASS

    
