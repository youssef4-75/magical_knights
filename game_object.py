


from abc import ABC

import pygame as pg

from vector import Vector


class GameObject(ABC):
    def __init__(self, left, top, width, height, color) -> None:
        super().__init__()
        self.__rect = pg.Rect(left, top, width, height)
        self.__surf = pg.Surface((width, height))
        self.__surf.fill(color)
        self.__vel = Vector()
        self.__accel = Vector()
    
    @property
    def rect(self):
        return self.__rect

    @property
    def surf(self):
        return self.__surf
    
    @property
    def accel(self):
        return self.__accel

    def move(self, direction: Vector):
        direction = direction.normalize() * self.speed
        direction.limit_ip(70)
        self.__rect.move_ip(direction.x, direction.y)

    def advance(self):
        self.__accel -= 0.2 * self.__vel
        self.__vel += self.__accel
        self.__vel.limit_ip(70)
        self.__rect.move_ip(self.__vel.x, self.__vel.y)
        self.__accel = Vector()

    def set_accel(self, accel: Vector):
        self.__accel = accel
