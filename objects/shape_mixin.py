import pygame as pg

from utils.mixin import Mixin



class ShapeMixin(Mixin):
    def __init__(self, ):
        self.__surf: pg.Surface; self.__animation_active: bool

    @staticmethod
    def start(self, width, height, color):
        self.__surf = pg.Surface((width, height))
        if color is not None: 
            self.__surf.fill(color)
        self.__animation_active = False
    
    @property
    def surf(self):
        return self.__surf
    
    def advance_surf(self):
        if not self.__animation_active:
            return

    def attach_animation(self):
        ...