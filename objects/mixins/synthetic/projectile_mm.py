import pygame as pg
from utils import Vector
from ..essence.motion_mixin import MotionMixin


class ProjectileMM(MotionMixin):

    def advance_rect(self):
        super().advance_rect()
        self.move(self.vel)
