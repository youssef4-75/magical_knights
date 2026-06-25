from icecream import ic
import pygame as pg

from ....utils import Mixin,  Pointable, K_FRICTION, SPEED_LIMIT,  Vector


class MotionMixin(Mixin, Pointable):

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

    def advance_rect(self, SPEED_LIMIT=None):
        self.__accel -= K_FRICTION * self.__vel
        self.__vel += self.__accel
        self.move(self.__vel, SPEED_LIMIT)
        self.__accel = Vector()

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y

    # ------ 
    def move_in_direction(self, direction: Vector, SPEED_LIMIT=None):
        velocity = direction.normalize() * self.speed
        self.move(velocity, SPEED_LIMIT)

    def move(self, velocity: Vector, SPEED_LIMIT=None):
        if SPEED_LIMIT:
            velocity.limit_ip(SPEED_LIMIT)
        self.__rect.move_ip(velocity.x, velocity.y)

    def set_accel(self, accel: Vector):
        self.__accel += accel

    def set_speed(self, value: int, SPEED_LIMIT: int = SPEED_LIMIT):
        if value < SPEED_LIMIT:
            self.__speed = value