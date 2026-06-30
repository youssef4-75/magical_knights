from game_env import MotionMixin, Vector



class VerticalMM(MotionMixin):
    def set_constant_mm(self, *, SPEED_LIMIT, HEIGHT, **_):
        self.__SPEED_LIMIT = SPEED_LIMIT
        self.__HEIGHT = HEIGHT

    def move(self, velocity: Vector):
        if self.__SPEED_LIMIT:
            velocity.limit_ip(self.__SPEED_LIMIT)
        if self.rect.top <= 0: 
            velocity = Vector(0, max(0, velocity.y))
        elif self.rect.bottom >= self.__HEIGHT:
            velocity = Vector(0, min(0, velocity.y))
        self.rect.move_ip(0, velocity.y)