


from abc import ABC, abstractmethod

from objects import GameObject


class Translater(ABC):
    @abstractmethod
    def translate(self, obj: GameObject):
        ...
