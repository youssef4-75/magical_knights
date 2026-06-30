



from random import randint

from ..essence.motion_mixin import MotionMixin



class BallMM(MotionMixin):
    def set_constant_mm(self, *, SPEED_LIMIT, HEIGHT):
        self.__SPEED_LIMIT = SPEED_LIMIT
        self.__HEIGHT = HEIGHT

    def advance_rect(self):
        # print(self.vel, self.vel.magnitude())
        self.vel.normalize_ip()
        if self.rect.top <= 0 or self.rect.bottom >= self.__HEIGHT:
            self.vel.y *= -1
        self.move(self.speed * self.vel, self.__SPEED_LIMIT)

    def reflect(self):
        self.vel.x *= -1
        r = self.speed//10
        self.vel.y += randint(-r, +r)
        self.vel.normalize_ip()