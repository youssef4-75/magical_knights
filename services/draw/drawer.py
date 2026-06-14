



from abc import ABC, abstractmethod

from screen import Window
from objects import GameObject


class Drawer(ABC):
    @abstractmethod
    def draw(self, window: Window, obj: GameObject):
        ...