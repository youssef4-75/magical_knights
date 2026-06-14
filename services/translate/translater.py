


from abc import ABC, abstractmethod

from objects import GameObject


class Translator(ABC):
    @abstractmethod
    def translate(self, obj: GameObject):
        ...
