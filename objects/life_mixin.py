


from utils.mixin import Mixin


class LifeMixin(Mixin):
    def __init__(self) -> None:
        self.__TTL: int; self.__HP: int

    @staticmethod
    def start(self, TTL: int, HP: int):
        self.__HP = HP
        self.__TTL = TTL

    @property
    def HP(self): return self.__HP

    @property
    def TTL(self): return self.__TTL

    def is_alive(self):
        return self.__TTL > 0 and self.__HP > 0

    def advance_life(self):
        self.__TTL -= 1

    def damage(self, amount):
        self.__HP -= amount 
        self.__HP = max(0, self.__HP)