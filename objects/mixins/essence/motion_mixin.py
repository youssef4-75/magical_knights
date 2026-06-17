import pygame as pg

from utils import Mixin,  Pointable, K, SPEED_LIMIT,  Vector


class MotionMixin(Mixin, Pointable):
    def __init__(self) -> None:
        self.__rect: pg.Rect; self.__vel: Vector; 
        self.__accel: Vector; self.__speed: int

    @staticmethod
    def start(self, left, top, width, height, 
            speed, vel: Vector|None=None, 
            accel: Vector|None=None):
        self.__rect = pg.Rect(left, top, width, height)
        self.__vel = Vector() if not vel else vel 
        self.__accel = Vector() if not accel else accel 
        self.__speed = speed

    @property
    def rect(self):
        return self.__rect 

    @property
    def accel(self):
        return self.__accel

    @property
    def vel(self):
        return self.__vel

    @property
    def speed(self):
        return self.__speed

    def advance_rect(self):
        self.__accel -= K * self.__vel
        self.__vel += self.__accel
        self.__vel.limit_ip(SPEED_LIMIT)
        self.__rect.move_ip(self.__vel.x, self.__vel.y)
        self.__accel = Vector()

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y

    # ------ 
    def move(self, direction: Vector):
        direction = direction.normalize() * self.speed
        direction.limit_ip(SPEED_LIMIT)
        self.__rect.move_ip(direction.x, direction.y)

    def set_accel(self, accel: Vector):
        self.__accel += accel

    def set_speed(self, value: int):
        if value < SPEED_LIMIT:
            self.__speed = value