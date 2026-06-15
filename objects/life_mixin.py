


from utils.mixin import Mixin


class LifeMixin(Mixin):
    def __init__(self) -> None:
        self.__TTL: int; self.__HP: int; self.__MP: int 

    @staticmethod
    def start(self, TTL: int, HP: int, MP: int):
        self.__HP = HP
        self.__TTL = TTL
        self.__MP = MP

    @property
    def HP(self): return self.__HP

    @property
    def TTL(self): return self.__TTL

    @property 
    def MP(self): return self.__MP

    def is_alive(self):
        return self.__TTL > 0 and self.__HP > 0 and self.__MP > 0

    def advance_life(self):
        self.__TTL -= 1

    def damage(self, amount):
        self.__HP -= amount 
        self.__HP = max(0, self.__HP)

    def consume(self, amount):
        if amount > self.__MP:
            return False 
        self.__MP -= amount 
        return True 

    def die(self):
        print(f"{self} has died")

    def born(self):
        print(f"{self} has born")