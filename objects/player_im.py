


from utils.mixin import Mixin


class PlayerIM(Mixin):
    def __init__(self) -> None:
        self.__MP: int

    @staticmethod
    def start(self, MP):
        self.__MP = MP

    @property
    def MP(self): return self.__MP

    def consume(self, energy: int):
        self.__MP -= energy

