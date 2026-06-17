
import pygame as pg

from ..mixins.synthetic import ProjectileMM, BallSM
from utils import Vector

from utils import ENERGY_SIZE, ENERGY_CLASS

from ..game_object import GameObject

class Energy(BallSM, ProjectileMM, GameObject):
    def __init__(self, init_pos, speed, direction: Vector, TTL: int = 200, color="red"):
        super().__init__(*init_pos, ENERGY_SIZE, 
                ENERGY_SIZE, speed=speed,
                TTL=TTL, HP=10, vel=direction, color=color)
        BallSM.start(self, ENERGY_SIZE, color)
        

    def typeIdentifier(self):
        return ENERGY_CLASS

    
