


from ....utils import Mixin


class LifeMixin(Mixin):
    def set_constant_lm(self, **kwargs):
        return

    # @staticmethod
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

    def damage(self, HP_damage):
        self.__HP -= HP_damage 
        self.__HP = max(0, self.__HP)

    def consume(self, MP_amount):
        if MP_amount > self.__MP:
            return False 
        self.__MP -= MP_amount 
        return True 

    def die(self, game=None):
        # print(f"{self} has died")
        ...

    def born(self, game=None):
        # print(f"{self} has born")
        ...