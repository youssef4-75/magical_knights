



from abc import ABC, abstractmethod

from pygame import Window

from game_object import GameObject
from player import Player


class Drawer(ABC):
    @abstractmethod
    def draw(self, window: Window, obj: GameObject):
        ...