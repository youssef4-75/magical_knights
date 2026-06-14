


class PlayerInteraction:
    def __init__(self, HP, MP) -> None:
        self.__HP = HP
        self.__MP = MP

    def damage(self, damage: int):
        print(f"received damage: {damage}, HP remaining: {self.__HP}")
        self.__HP -= damage

    def consume(self, energy: int):
        self.__MP -= energy

    def is_alive(self):
        return self.__HP > 0