


from abc import ABC, abstractmethod

import pygame as pg

from utils import Vector, K, SPEED_LIMIT


class GameObject(ABC):
    def __init__(self, left, top, width, height, color) -> None:
        super().__init__()
        self.__rect = pg.Rect(left, top, width, height)
        self.__surf = pg.Surface((width, height))
        self.__surf.fill(color)
        self.__vel = Vector()
        self.__accel = Vector()
    
    @abstractmethod
    def typeIdentifier(self): ...
    
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
        direction.limit_ip(SPEED_LIMIT)
        self.__rect.move_ip(direction.x, direction.y)

    def advance(self):
        self.__accel -= K * self.__vel
        self.__vel += self.__accel
        self.__vel.limit_ip(SPEED_LIMIT)
        self.__rect.move_ip(self.__vel.x, self.__vel.y)
        self.__accel = Vector()

    def set_accel(self, accel: Vector):
        self.__accel = accel

    @abstractmethod
    def draw(self, window):
        """this tells the drawer manager how this object is drawn in the window"""
        ...

    @abstractmethod
    def translate(self):
        """this tells the translator manager how this objects receive motions from the user input"""
        ...