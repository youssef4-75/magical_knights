import pygame as pg


from ..essence.shape_mixin import ShapeMixin



class BallSM(ShapeMixin):

    @staticmethod
    def start(self, radius, color):
        self.__ball_surf = BallSM.create_circle_surface(radius, color)
        self.__color = color
        self.__animation_active = False
    
    @staticmethod
    def create_circle_surface(radius: int, color: tuple, alpha: bool = True) -> pg.Surface:
        """Create a circular surface."""
        size = radius * 2
        surface = pg.Surface((size, size), pg.SRCALPHA if alpha else 0)
        pg.draw.circle(surface, color, (radius, radius), radius)
        return surface

    @property
    def surf(self):
        return self.__ball_surf

