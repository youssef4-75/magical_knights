from icecream import ic
import pygame as pg


from ....utils import Mixin,  Pointable, SPEED_LIMIT,  Vector


class MotionMixin(Mixin, Pointable):

    def set_constant_mm(self, *, SPEED_LIMIT=SPEED_LIMIT, **_):
        print("here")
        self.__SPEED_LIMIT = SPEED_LIMIT

    def start(self, left, top, width, height, 
            speed, vel: Vector|None=None, 
            accel: Vector|None=None, *_, **__):
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

    @accel.setter
    def accel(self, value):
        self.__accel = value

    @property
    def vel(self):
        return self.__vel

    @vel.setter
    def vel(self, value):
        self.__vel = value

    @property
    def speed(self):
        return self.__speed

    def advance_rect(self):
        self.__vel += self.__accel
        self.move(self.__vel)
        self.__accel = Vector()

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y

    # ------ 
    def move_in_direction(self, direction: Vector, ):
        velocity = direction.normalize() * self.speed
        self.move(velocity)

    def move(self, velocity: Vector):
        if self.__SPEED_LIMIT:
            velocity.limit_ip(self.__SPEED_LIMIT)
        self.__rect.move_ip(velocity.x, velocity.y)

    def add_accel(self, accel: Vector):
        self.__accel += accel

    def set_speed(self, value: int):
        if value < self.__SPEED_LIMIT:
            self.__speed = value