


from abc import ABC, abstractmethod

from game_object import GameObject
from window import Window


class Translater(ABC):
    @abstractmethod
    def translate(self, obj: GameObject):
        ...
